from bs4 import BeautifulSoup
from selenium import webdriver


def get_data():
    driver = webdriver.Chrome()
    driver.get('https://www.facebook.com/events/290444603568318')
    # html = driver.page_source

    # soup = BeautifulSoup(html, 'html.parser')
    # result = soup.find('div', class_=['2ycp', '_5xhk'])
    # driver.close()

    # return result
    # driver.get("https://www.python.org")
    return driver.title
