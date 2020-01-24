import requests

class Webcrawler():
  request_count = 0
  
  def __init__(self, root_url=None, SITEMAP={}, AUTORUN=False):
    self.url = root_url
    self.sitemap = SITEMAP
    self.externallinks = []
    self.contentlinks = []
    self.discoverable = []
    self.visited = []
    self.url_history = []
    self.response_history = []
    self.pagenodes = []
    self.response = None
    self.success = None
    self.autorun = AUTORUN

    if self.url is not None: 
      self.sitemap[self.url] = {'pageNode':None}
      self.get_url()
      if self.autorun is True:
        self.autorun()

  def get_url(self, url=None):
    if url is not None:
      self.url = url
    try:
      if self.url not in self.visited:
        self.response = requests.get(self.url)
        self.visited.append(self.url)
        self.response_history.append(self.response)
        self.analyze_response()  
        Webcrawler.request_count += 1
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

  def autorun(self):
    return self.get_url(self.discoverables.pop(0))

class PageNode():
  total_nodes = 0
  num_nodes = 0

  def __init__(self, url, response):
    self.node_url = url
    self.response = response
    self._parent = None  
    self._children = None
    self.sitelinks = []
    self.externallinks = []
    self.contentlinks = []
    self.htmlcontent = []
    self.javascriptlinks = []
    self.csslinks = []
    self.node_id = PageNode.total_nodes
    PageNode.total_nodes += 1
    PageNode.num_nodes += 1

  def __del__(self):
    PageNode.num_nodes -= 1 
