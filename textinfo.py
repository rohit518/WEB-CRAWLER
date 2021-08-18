from bs4 import BeautifulSoup
def relevant_data_section(html_file):
    stack=list()
    soup=BeautifulSoup(html_file, 'html.parser')
    for link in soup.find_all('p'):
        stack.append(link.text)
    return stack