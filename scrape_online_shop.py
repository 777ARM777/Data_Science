import time
import scraping_with_BeautifulSoup as sbs
from selenium import webdriver
from selenium.webdriver.common.by import By


def scrape_with_selenium(url):
    driver = webdriver.Edge()

    try:
        driver.get(url)
        sidebar_items = driver.find_elements(By.CSS_SELECTOR, '#side-menu > li.nav-item')[1:]

        for sidebar_item in sidebar_items:
            sidebar_item.click()
            categories = driver.find_elements(By.CSS_SELECTOR, '.sidebar .active .nav-item')

            for category in categories:
                category.click()
                soup = sbs.scrap_data(driver.current_url)
                with open('scraped_data_selenium.txt', 'a') as file:
                    sbs.store_in_file(soup, file)

                time.sleep(1)
                driver.back()
            driver.back()

    except Exception as err:
        print(str(err))
    finally:
        driver.quit()


if __name__ == '__main__':
    url = 'https://webscraper.io/test-sites/e-commerce/allinone'
    soup = sbs.scrap_data(url)
    with open('scraped_data_selenium.txt', 'w') as file:
        sbs.store_in_file(soup, file)

        scrape_with_selenium(url)
