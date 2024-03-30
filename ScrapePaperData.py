import requests
from bs4 import BeautifulSoup

url_trending = 'https://paperswithcode.com/'
url_latest = 'https://paperswithcode.com/latest'
url_greatest = 'https://paperswithcode.com/greatest'

def get_trending_papers_data(url:str) ->list:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a')
    root = 'https://paperswithcode.com'
    filtered_links = []
    for link in links:
        href = link.get('href')
        try:
            if href.startswith('/paper'):
                href = href.split('#')[0]
                filtered_links.append(root + href)
        except:
            pass
            
    filtered_links = list(set(filtered_links))
    return filtered_links

trending_url_list = get_trending_papers_data(url_trending)
latest_url_list = get_trending_papers_data(url_latest)
greatest_url_list = get_trending_papers_data(url_greatest)
