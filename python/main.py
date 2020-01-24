from Webcrawler import Webcrawler

crawler = Webcrawler("http://wiprodigital.com")
print(crawler.discoverable)
print(" ")
print(crawler.pagenodes[0].sitelinks)
print(" ")
print(crawler.pagenodes[0].externallinks)
print(" ")
print(crawler.pagenodes[0].contentlinks)
