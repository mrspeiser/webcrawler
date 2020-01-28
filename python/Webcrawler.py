import requests
import re
from bs4 import BeautifulSoup

class Webcrawler():
  request_count = 0
  
  def __init__(self, root_url=None, SITEMAP={}, Response=None, AUTORUN=False):
    self.url = root_url
    self.sitemap = SITEMAP
    self.currentnode = ""
    self.sitelinks = []
    self.externallinks = []
    self.contentlinks = []
    self.htmlcontent = []
    self.javascriptlinks = []
    self.csslinks = []
    self.discoverable = []
    self.visited = []
    self.url_history = []
    self.response_history = []
    self.pagenodes = []
    self.response = Response
    self.success = None
    self._parent = None  
    self._children = None
    self.autorun = AUTORUN

    if self.url is not None: 
      self.sitemap[self.url] = {'pageNode':None}
      self.currentnode = self.sitemap[self.url]
      self.get_url()
      if self.autorun is True:
        self.autorun()

  def get_url(self, url=None):
    if url is not None:
      self.url = url
    try:
      if self.url not in self.visited:
        print(f'getting {self.url}')
        self.response = requests.get(self.url)
        self.visited.append(self.url)
        self.response_history.append(self.response)
        self.analyze_response()  
        Webcrawler.request_count += 1
        self.update_sitemap()
        return True
    except requests.exceptions.MissingSchema as requests_error:
      print('error, no url schema, bad request')
      self.success = False
      return False

  def analyze_response(self):
    if self.response.status_code == 200:
      self.success = True
      page = PageNode(self.url, self.response)
      self.pagenodes.append(page)
      discoverables = [ x for x in page.sitelinks if x not in self.visited ]
      self.discoverable += discoverables
      return True
    else:
      self.success = False
      return False

  def update_sitemap(self):
    for link in self.discoverable:
      self.currentnode[link] = {'_pagenode':None} 

  def autorun(self):
    self.discoverable.append(self.url)
    while len(self.discoverable) is not 0:
      self.get_url(self.discoverable.pop(0))

# every url is a dictionary that is required to have a _pagenode key
#self.sitemap = {   
#  "http://wiprodigil.com": { 
#    "disocveredurl": {
#        "innerdiscoveredurl": {
#          "innerinnerdisc": {
#            "pagenode":PageNode
#          },
#          "pagenode":PageNode
#        },
#        "pagenode"PageNode
#      }
#    "pagenode":PageNode
#    }
#  }
#self.sitemap = { "rootnode": {"_pagenode":None}}
class PageNode(Webcrawler):

  """
    The PageNode class represents a page that has been crawled by the Webcrawler

    The PageNode has the ability to spawn new Webrawlers because itself is also a Webcrawler by inheriting its methods and properties;
    
    Required Parameters:
      1. The URL that was used to make the request
      2. The response from the requests.get() call

    Important Data Properties:
      1. self.sitelinks: A list of hrefs from <a> tags that have that matches the qualified domain name of the URL e.g: "wiprodigital.com"
      2. self.externallinks: A list of hrefs from <a> tags that DO NOT match  the qualified domain name of the URL e.g: "wiprodigital.com"
      3. self.contentlinks: A list of src attributes from img tags

  """

  total_nodes = 0
  num_nodes = 0

  def __init__(self, url, response, Parent=None):
    super().__init__(self, Response=response)
    self.node_url = url
    self.node_id = PageNode.total_nodes
    PageNode.total_nodes += 1
    PageNode.num_nodes += 1
    self.soup = BeautifulSoup(response.content, 'html.parser') 
    self.scan_hrefs()
    self.scan_content_links()
    #self.get_children()

  def __del__(self):
    PageNode.num_nodes -= 1 

  def scan_hrefs(self):
    atags = self.soup.find_all("a")
    hrefs = [ link.attrs['href'] for link in atags ]
    qdn = re.search("://", self.node_url)
    if qdn is not None:
      span = qdn.span()[1]
      qdn = self.node_url[int(span)::]
      qdn = qdn.split('/')[0]

    uniquelinks = set(hrefs)
    for i in uniquelinks:
      x = re.search(qdn, i)
      if x is not None:
        self.sitelinks.append(i)
        
      else:
        self.externallinks.append(i)

  def scan_content_links(self):
    srcs = [ img['src'] for img in self.soup.find_all("img") ]
    self.contentlinks = set(srcs)

  def get_children(self):
    for link in self.sitelinks:
      self.get_url(link)

