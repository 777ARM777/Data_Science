import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone'

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
    for link in soup.find_all(class_="card-body"):
        print(link.find(class_="title").get('title'))
        print(link.find(class_='float-end price card-title pull-right').text)
        print(link.find(class_='float-end review-count').text)



