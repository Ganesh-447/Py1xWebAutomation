import time

from selenium import webdriver
import pytest
import logging


def test_open_browser():
    # Hierarchy - python code - selenium 4 server - webdriver - browser

    chrome_options = webdriver.ChromeOptions()
    # extension_path = "/Users/apple/Downloads/adblocker.crx"
    # chrome_options.add_extension(extension_path)
    #chrome_options.add_argument("--start-maximized")

    #driver = webdriver.Chrome(options=chrome_options)  #fresh doesn't have anything


    driver = webdriver.Chrome()  # ->post request to get chrome
    LOGGER = logging.getLogger(__name__)
    driver.get("https://google.com")
    driver.maximize_window()
    LOGGER.info(driver.title)
    time.sleep(20000)
