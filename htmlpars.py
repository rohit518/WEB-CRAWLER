from html.parser import HTMLParser
from urllib import parse
class Find_Link(HTMLParser):
    def __init__(self,base_url,page_url):
        super().__init__()
        self.base_url=base_url
        self.page_url=page_url
        self.urls=set()
    def handle_starttag(self,tags,attrs):
        if tags=='a':
            for(attribute,value) in attrs:
                if attribute =='href':
                    url= parse.urljoin(self.base_url,value)
                    self.urls.add(url)
    def all_provided_links(self):
        return self.urls
    def error(self,message):
        pass