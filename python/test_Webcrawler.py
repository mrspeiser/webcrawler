import unittest
from Webcrawler import Webcrawler, PageNode

class test_Webcrawler(unittest.TestCase):

  def test_initialize(self):
    crawler0 = Webcrawler()
    self.assertTrue(hasattr(crawler0, 'url'))
    self.assertTrue(hasattr(crawler0, 'sitemap'))
    self.assertTrue(hasattr(crawler0, 'pagenodes'))
    self.assertTrue(hasattr(crawler0, 'externallinks'))
    self.assertTrue(hasattr(crawler0, 'contentlinks'))
    self.assertTrue(hasattr(crawler0, 'visited'))

  def test_defined_methods(self):
    crawler = Webcrawler()
    methods = ['get_url']
    for m in methods:
      self.assertTrue(callable(getattr(crawler, m)))

class test_PageNode(unittest.TestCase):
  
  def test_initialize(self):
    pagenode0 = PageNode()
    self.assertTrue(hasattr(pagenode0, '_parent'))
    self.assertTrue(hasattr(pagenode0, '_children'))
    self.assertTrue(hasattr(pagenode0, 'sitelinks'))
    self.assertTrue(hasattr(pagenode0, 'externallinks'))
    self.assertTrue(hasattr(pagenode0, 'contentlinks'))
    self.assertTrue(hasattr(pagenode0, 'htmlcontent'))
    self.assertTrue(hasattr(pagenode0, 'javascriptlinks'))
    self.assertTrue(hasattr(pagenode0, 'csslinks'))

  def test_nodes_count(self):
    pagenode0 = PageNode()
    pagenode1 = PageNode()
    self.assertEqual(pagenode0.num_nodes, 2)
    self.assertEqual(pagenode0.node_id, 1)
    self.assertEqual(pagenode1.num_nodes, 2)
    self.assertEqual(pagenode1.node_id, 2)

if __name__ == '__main__':
  unittest.main()
