import requests
from bs4 import BeautifulSoup
from googlesearch import search

# university = input("Enter University Name")

def get_links(university):
    urls = []
    query = f"{university} university academic programs"
    for j in search(query, num=10, stop=10, pause=5):
        urls.append(j)
        # print(j)
    return urls



def get_content(url):
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, "html.parser")
    body = soup.find("body")
    body_list = [i.text.strip().split('\n') for i in body]
    content_list = [k.strip() for j in body_list if j != [''] for k in j if j != '']
    content_list2 =  [text for text in content_list if text != '']
    return content_list2
