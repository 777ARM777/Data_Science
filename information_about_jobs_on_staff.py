import requests
import time
import csv

from selenium.webdriver.common.by import By
from requests.exceptions import HTTPError
from selenium import webdriver
from bs4 import BeautifulSoup


def store_in_file(soup, writer):

    for link in soup.find_all(class_="web_item_card hs_job_list_item"):
        row = [link.find(class_="font_bold").text.replace('\n', '').strip(),
               link.find(class_='job_list_company_title').text.replace('\n', '').strip(),
               link.find(class_='formatted_date').text.replace('\n', '').strip(),
               link.find(class_='job_location').text.replace('\n', '').strip()]
        writer.writerow(row)



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


def scrape_with_selenium(url, header):
    driver = webdriver.Edge()

    try:
        driver.get(url)
        categories = driver.find_elements(By.CLASS_NAME, 'hs_nav_link')
        categories[0].click()
        time.sleep(1)
        soup = scrap_data(driver.current_url)


        with open('staff_am_data.csv', 'w', encoding='UTF8', newline='') as file:
            for i in range(27):
                writer = csv.writer(file)
                writer.writerow(header)
                store_in_file(soup, writer)

                driver.find_element(By.CLASS_NAME, 'next').click()
                print(driver.current_url)



    except Exception as err:
        print(str(err))
    finally:
        driver.quit()


if __name__ == '__main__':
    url = 'https://staff.am/en/'
    header = ['job_name', 'company', 'deadline', 'location']

    scrape_with_selenium(url, header)
