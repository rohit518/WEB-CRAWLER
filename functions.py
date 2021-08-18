import os
from urllib.parse import urlparse
def makeproject(name):
    if not os.path.exists(name):
        print("Creating new directory." +name)
        os.makedirs(name)
def queue_crawl_index(name,url):
    queue=name + '/queue.txt'
    crawl=name + '/crawl.txt'
    indexer=name +'/indexer.txt'
    if not os.path.isfile(queue):
        create_file(queue,url)
    if not os.path.isfile(crawl):
        create_file(crawl,'')
    if not os.path.isfile(indexer):
        create_file(indexer,'')
def create_file(path,content):
    file=open(path,'w')
    file.write(content)
    file.close()
def appendfile(path,content):
    with open(path,'a',encoding='utf-8') as file:
        file.write(content+ '\n')
def undofile(path):
    with open(path,'w'):
        pass
def set_conversion(path):
    ans=set()
    with open(path,'rt') as file:
        for line in file:
            ans.add(line.replace('\n',''))
    return ans
def list_conversion(path):
    ans=list()
    with open(path,'rt') as file:
        for line in file:
            ans.append(line.replace('\n',''))
    return ans
def file_conversion(urls,path):
    undofile(path)
    for links in sorted(urls):
        appendfile(path,links)
def list_to_file(paragraphs,path):
    undofile(path)
    for frames in paragraphs:
        appendfile(path,frames)
def get_project_and_domain_signature(link):
    try:
        ans=get_subdomain(link).split('.')
        return ans[-2],ans[-2]+'.'+ans[-1]
    except:
        return ''
def get_subdomain(link):
    try:
        return urlparse(link).netloc
    except:
        return ''


