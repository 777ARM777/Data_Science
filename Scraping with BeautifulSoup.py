import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup


def store_in_file(soup, file):
    for link in soup.find_all(class_="card-body"):
        file.write('Title: ' + link.find(class_="title").get('title') + '\n')
        file.write('Price: ' + link.find(class_='float-end price card-title pull-right').text + '\n')
        file.write('Reviews: ' + link.find(class_='float-end review-count').text + '\n\n')


def scrap_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    else:
        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        return soup


if __name__=='__main__':
    url = 'https://webscraper.io/test-sites/e-commerce/allinone'
    soup = scrap_data(url)
    with open('scraped_data.txt', 'w') as file:
        store_in_file(soup, file)
