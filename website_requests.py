import requests
from requests.exceptions import HTTPError


URLS = ['https://en.wikipedia.org/wiki/Picsart', 'https://en.wikipedia.org/wiki/Armenia', 'https://en.wikipedia.org/wiki/Yerevan',
        'https://en.wikipedia.org/wiki/English_language', 'https://en.wikipedia.org/wiki/United_States_House_of_Representatives',
        'https://en.wikipedia.org/wiki/Harvard_University', 'https://en.wikipedia.org/wiki/Yerevan_State_University']

for url in URLS:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    else:
        print(response.text)
