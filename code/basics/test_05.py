import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import logging


def test_texlink():
    driver = webdriver.Chrome()
    driver.get("https:/app.vwo.com")
    time.sleep(2)
    text_link = driver.find_element(By.LINK_TEXT,"Start a free trial").click()
    time.sleep(2)
    print(driver.name)
