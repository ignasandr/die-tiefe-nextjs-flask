# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def get_data():
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")

    remote_url = "https://bot.kmn.lt"

    driver = webdriver.Remote(
        command_executor=remote_url,
        options=options
    )
    driver.get("https://www.libib.com/u/kmnskaitykla")

    time.sleep(3)  # replace with WebDriverWait

    page_title = driver.title
    published_count = int(driver.find_element(
        By.CLASS_NAME, 'published-library-count').text)

    second_position = driver.execute_script(
        "return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)  # Wait for additional content to load
    third_position = driver.execute_script("return document.body.scrollHeight")

    items = []

    while True:
        # driver.find_element(By.ID, 'library-items-wrapper').send_keys(Keys.END)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)  # Wait for additional content to load
        new_items = driver.find_elements(By.CLASS_NAME, 'item')
        # if len(new_items) >= published_count:
        #     break  # No new items loaded, end loop
        if len(new_items) == len(items):
            break
        items = new_items

    scraped_data = []

    for item in items:
        image_url = item.find_element(By.TAG_NAME, 'img').get_attribute('src')
        text_content = item.find_element(By.CLASS_NAME, 'item-title').text

        scraped_data.append(
            {"Image URL": image_url, "Text Content": text_content})

    driver.quit()

    # return {"Page title": page_title, "Page text": scraped_data, "Publihed Count": published_count}
    return {"Page title": page_title, "Page text": scraped_data, "Publihed Count": published_count, "First": first_position, "Second": second_position, "Third": third_position}
