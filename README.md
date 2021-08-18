
# WEB-CRAWLER

This is a single threaded(a single spider object crawling) 
web crawler. The crawler is designed to get the HYPERLINKS and the 
TEXT data in the homepage of any website by taking an url as the user input.
The crawler again crawls all the gathered urls.This is a 2-level crawling.

After crawling all the relevant links and 
paragraphs and storing them in different files.




## Overview
The complete code is in python.Two of the primary modules used in the 
code are HTMLParser and beautifulsoup4. A document is attached with code explanation,
diagram and screenshots for reference.

- HTMLParser-This module provides us with the HTMLParser class, 
  which can be sub-classed to parse HTML-formatted text files.
  Here it is used to get the hyperlinks from the anchor tags in html docs.

  More About HTMLparser-https://github.com/PolicyStat/HTMLParser/

- beautifulsoup4-It is a library that makes it easy to 
  scrape information from web pages.Here it is used to extract the 
  text data from a website's page.

  More About beautifulsoup4-https://pypi.org/project/beautifulsoup4/

After running the main.py file 
the result is rendered on the terminal.Also a new folder named
according to the domain name(in most cases) is created which contains
three text files.

- queue.txt-It contains the hyperlinks from the base page.

- crawl.txt-Crawls all the urls from queue.txt and adds here.

- indexer.txt-has all the text data collected.

  ## Dependencies
```bash
pip install beautifulsoup4
```
```bash
pip install HTMLParser
```
## Deployment

To deploy this project first clone the repository 
using git command or by downloading the zip file.
Now forward to the downloaded directory.Run the main.py file.

```bash
  python main.py
```
 
  
## Acknowledgements
Thanks to the youtube channel-[thenewboston](https://www.youtube.com/watch?v=nRW90GASSXE&list=PL6gx4Cwl9DGA8Vys-f48mAH9OKSUyav0q)


  
