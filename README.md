## Buildit Webcrawler Assignment

#### Specification:
1. The crawler should be limited to one domain "http://wiprodigital.com"
2. The crawler should visit all pages within the domain, but not follow the links to external sites eg. Google Twitter
3. The Crawler should be able to output a simple structured site map (something that clearly defines what the crawler has discovered)
4. Shows links to other pages under same domain, links to external URLs, and static content

#### Usage Expectation:

When using this webcrawler it should be very simple and straight forward to import and run.

If this is implemented using Python I would expect to use it by simply doing:

```
from Webcrawler import Webcrawler
crawler = Webcrawler('http://wiprodigital.com')
crawler.sitemap
crawler.externallinks
crawler.contenturls
```

If this is implemented in Nodejs I would expect to use it by simply doing:

```
const webcrawler = require("Webcrawler.js")
let crawler = new Webcrawler('http://wiprodigital.com')
crawler.on('done', (crawler) => {
  crawler.sitemap
  crawler.externallinks
  crawler.contenturls
}
```
