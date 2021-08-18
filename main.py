from functions import get_project_and_domain_signature,set_conversion
from crawler import Spider
home_page=str(input("Enter the base address to crawl:"))
project,domain=get_project_and_domain_signature(home_page)
Spider(project,home_page,domain)
url_set=set_conversion(project+"/queue.txt")
i=2
for links in url_set:
    Spider.crawlpage(links)
    i=i+1
print("\n")
print("Total "+str(len(set_conversion(project+"/crawl.txt")))+ " links crawled.")
