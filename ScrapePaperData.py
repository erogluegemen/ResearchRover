import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url_trending = 'https://paperswithcode.com/'
url_latest = 'https://paperswithcode.com/latest'
url_greatest = 'https://paperswithcode.com/greatest'

def get_trending_papers_data(url:str) ->list:
    # Send a GET request to the URL and store the response
    response = requests.get(url)

    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the links on the page
    links = soup.find_all('a')

    # Define root url
    root = 'https://paperswithcode.com'

    # Filter the links based on their href attribute
    filtered_links = []
    for link in links:
        href = link.get('href')
        try:
            if href.startswith('/paper'):
                href = href.split('#')[0]
                filtered_links.append(root + href)
        except:
            pass

    # Remove the duplicated items    

    filtered_links = list(set(filtered_links))

    # Return the filtered links
    return filtered_links

trending_url_list = get_trending_papers_data(url_trending)
latest_url_list = get_trending_papers_data(url_latest)
greatest_url_list = get_trending_papers_data(url_greatest)