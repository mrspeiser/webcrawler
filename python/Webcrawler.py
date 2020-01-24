import requests

class Webcrawler():

  def __init__(self, URL=None, SITEMAP=[]):
    self.url = URL
    self.sitemap = SITEMAP
    self.externallinks = []
    self.contentlinks = []
    self.visited = []
    self.pagenodes = []

  def get_url(self):
    pass


class PageNode():
  total_nodes = 0
  num_nodes = 0

  def __init__(self, url=""):
    self.node_url = url
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
