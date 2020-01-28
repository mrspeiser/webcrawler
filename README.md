## Buildit Webcrawler Assignment

- [Specification](#specification)
- [Usage Expectation](#usage-expectation)
- [Testing](#testing)
- [Actual Implementation](#actual-implementation-details)
- [Requirements](#requirements)
- [Sitemap](#sitemap)
- [With More Time](#with-more-time)

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
print(crawler.sitemap)
print(crawler.externallinks)
print(crawler.contenturls)
```

If this is implemented in Nodejs I would expect to use it by simply doing:

```
const webcrawler = require("Webcrawler.js")
let crawler = new Webcrawler('http://wiprodigital.com')
crawler.on('done', (crawler) => {
  console.log(crawler.sitemap);
  console.log(crawler.externallinks);
  console.log(crawler.contenturls);
})
```

#### Testing:

To see if the crawler in Python is working:
1. navigate to the python directory
2. run ``` python test_Webcrawler.py ``` 


To see if the crawler in Javascript is working:
1. navigate to the nodejs directory
2. run ``` npm test ``` 

#### Actual Implementation Details:


The crawler was utlimately implemented with **Python** mainly because of not having to deal with extra async await calls for nodejs. Testing seemed a bit more straight forward and simpler to implement in a shorter amount of time.

##### Requirements:

1. requests ```pip install requests --user```
2. beautifulsoup ```pip install beautifulsoup4 --user```

##### Classes
There are 2 classes in the Webcrawler.py file:

1. Webcrawler
2. PageNode

You can pass an initial url to the Webcrawler class and it will automatically make a GET request to the page.
Currently, In order to view what the crawler discovered you must access the PageNode directly in the pagenodes list:

```
crawler = Webcrawler("http://wiprodigital.com")
print(crawler.pagenodes[0].sitelinks)
print(crawler.pagenodes[0].externallinks)
print(crawler.pagenodes[0].contentlinks)
```

Once the crawler finishes discovering a page it will add all the sitelinks from the PageNode to the "discoverable" property that are not already present in the "visited" property to ensure that the crawler doesn't go to the same page more than once.

**The Sitemap has not been fully implemented yet**

##### SiteMap

The sitemap is intended to be implemented as a nested dictionary.

The first key representing the root_url of the tree like data structure.

Each url named key has a value that is a dictionary that has a default '_pagenode' key, and all other sibling keys inside representing the site links that were discovered for that outer key url.

```
sitemap = {
  'root_url': {
    '_pagenode':None,
    'site_url1': {
      '_pagenode:None,
      'unique_inner_url1': {
        '_pagenode:None,
      },
      'unique_inner_url2': {
        '_pagenode:None,
      },
    }
    'site_url2': {
      '_pagenode:None,
      'unique_inner_url2-1': {
        '_pagenode:None,
    }
    'site_url3': {
      '_pagenode:None,
      'unique_inner_url3-1': {
        '_pagenode:None,
      },
      'unique_inner_url3-2': {
        '_pagenode:None,
      },
    }
  }
}
```

##### With More Time

1. The Webcrawler isn't finished and with more time I would have actually finished the functionality to actually visit each url discovered and fully finished the sitemap.
2. There are also issues with discovering urls with hash values attached to them that needs to be addressed
3. Cleanup and refactoring with PageNode class. I thought I wanted to recursively discover additional pages by having the PageNode itself discover the pages that it had internally. Now though I think it would be more straight forward with building the sitemap from the webcrawler class and allow the PageNode to just be a representation attached to the sitemap.
4. Created a cleaner visualization of the sitemap dictionary with arrows pointing to where the urls go to. Also if the same links were found on different pages I would want to link the '_pagenode' to the originally discovered PageNode.
