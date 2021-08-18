from functions import makeproject,queue_crawl_index,set_conversion,file_conversion,list_conversion,list_to_file
from textinfo import relevant_data_section
from htmlpars import Find_Link
import urllib.request
class Spider:
    project=''
    homepage_url=''
    domain=''
    queue=set()
    crawl=set()
    index=list()
    queue_text=''
    crawl_text=''
    indexer_text=''
    def __init__(self,project,homepage_url,domain):
        Spider.project=project
        Spider.homepage_url=homepage_url
        Spider.domain=domain
        Spider.queue_text=Spider.project+('/queue.txt')
        Spider.crawl_text=Spider.project+('/crawl.txt')
        Spider.indexer_text=Spider.project+('/indexer.txt')
        self.create_spider()
        self.crawlpage(Spider.homepage_url)
    @staticmethod
    def create_spider():
        makeproject(Spider.project)
        queue_crawl_index(Spider.project,Spider.homepage_url)
        Spider.queue=set_conversion(Spider.queue_text)
        Spider.crawl=set_conversion(Spider.crawl_text)
        Spider.indexer=list_conversion(Spider.indexer_text)
    @staticmethod
    def crawlpage(page):
        if page not in Spider.crawl:
            print('Queue '+str(len(Spider.queue))+'--Crawled '+str(len(Spider.crawl)))
            print(page+' crawled')
            links,paras=Spider.collect_links_from_page(page)
            Spider.add_to_queue(links)
            Spider.queue.remove(page)
            Spider.crawl.add(page)
            for content in paras:
                Spider.index.append(content)
            file_conversion(Spider.queue,Spider.queue_text)
            file_conversion(Spider.crawl,Spider.crawl_text)
            list_to_file(Spider.index,Spider.indexer_text)
    @staticmethod
    def collect_links_from_page(page):
        html=''
        try:
            temp = urllib.request.urlopen(page)
            bytes = temp.read()
            html = bytes.decode("utf-8")
            count=Find_Link(Spider.homepage_url,page)
            count.feed(html)
            k=relevant_data_section(html)
        except:
            print('Error 403:Forbidden')
            return set(),list()
        return count.all_provided_links(),k
    @staticmethod
    def add_to_queue(links):
        for tupples in links:
            if tupples in Spider.queue:
                continue
            if tupples in Spider.crawl:
                continue
            if Spider.domain not in tupples:
                continue
            Spider.queue.add(tupples)


