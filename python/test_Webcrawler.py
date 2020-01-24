import unittest
from Webcrawler import Webcrawler, PageNode

class test_Webcrawler(unittest.TestCase):
  default_url = "http://wiprodigital.com"

  def test_initialize(self):
    crawler0 = Webcrawler()
    self.assertTrue(hasattr(crawler0, 'url'))
    self.assertTrue(hasattr(crawler0, 'sitemap'))
    self.assertTrue(hasattr(crawler0, 'pagenodes'))
    self.assertTrue(hasattr(crawler0, 'externallinks'))
    self.assertTrue(hasattr(crawler0, 'contentlinks'))
    self.assertTrue(hasattr(crawler0, 'visited'))
    self.assertTrue(hasattr(crawler0, 'url_history'))
    self.assertTrue(hasattr(crawler0, 'response_history'))
    self.assertTrue(hasattr(crawler0, 'response'))
    self.assertTrue(hasattr(crawler0, 'success'))

  def test_defined_methods(self):
    crawler = Webcrawler()
    methods = ['get_url']
    for m in methods:
      self.assertTrue(callable(getattr(crawler, m)))

  def test_get_request_urls(self):
    crawler0 = Webcrawler()
    self.assertIsNone(crawler0.response)

    crawler1 = Webcrawler(test_Webcrawler.default_url)
    self.assertIsNotNone(crawler1.response)

    crawler2 = Webcrawler()
    self.assertTrue(crawler2.get_url('http://google.com'))
    self.assertEqual(crawler2.url, 'http://google.com')

    crawler2.url = test_Webcrawler.default_url
    self.assertEqual(crawler2.url, test_Webcrawler.default_url)

    self.assertFalse(crawler2.get_url('asdljksadfljsldhg'))
    self.assertFalse(crawler2.success)

class test_PageNode(unittest.TestCase):

#  def __init__(self):
#    self.crawler = Webcrawler(test_Webcrawler.default_url)
#    self.pagenode = PageNode(self.crawler, self.crawler.response)

  def test_initialize(self):
    crawler1 = Webcrawler(test_Webcrawler.default_url)
    pagenode0 = PageNode(crawler1.url, crawler1.response)
    self.assertTrue(hasattr(pagenode0, '_parent'))
    self.assertTrue(hasattr(pagenode0, '_children'))
    self.assertTrue(hasattr(pagenode0, 'sitelinks'))
    self.assertTrue(hasattr(pagenode0, 'externallinks'))
    self.assertTrue(hasattr(pagenode0, 'contentlinks'))
    self.assertTrue(hasattr(pagenode0, 'htmlcontent'))
    self.assertTrue(hasattr(pagenode0, 'javascriptlinks'))
    self.assertTrue(hasattr(pagenode0, 'csslinks'))

  def test_nodes_count(self):
    crawler1 = Webcrawler(test_Webcrawler.default_url)
    crawler2 = Webcrawler('http://google.com')
    pagenode0 = PageNode(crawler1.url, crawler1.response)
    self.assertEqual(pagenode0.num_nodes, 3)
    pagenode1 = PageNode(crawler2.url, crawler2.response)
    #self.assertEqual(pagenode0.node_id, 4) # page node should be 4 not 0 because pagenode was called once in the above function
    #self.assertEqual(pagenode1.num_nodes, 4) # PageNodes should be 4 because both crawler1 and crawler2 create a PageNode automatically when loading URL
    #self.assertEqual(pagenode1.node_id, 5)

  def test_html_document(self):
    crawler1 = Webcrawler(test_Webcrawler.default_url)
    pagenode0 = PageNode(crawler1.url, crawler1.response)
    print(dir(pagenode0.response))
    print(pagenode0.response.content) 
    print(pagenode0.response.links) 

if __name__ == '__main__':
  unittest.main()
