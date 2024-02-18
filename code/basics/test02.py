import time
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com")
    time.sleep(10)
    email_ele = driver.find_element(By.NAME, "username")
    password_ele = driver.find_element(By.NAME, "password")
    sign_in_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    email_ele.send_keys("Admin")
    password_ele.send_keys("admin123")
    sign_in_button.click()
    LOGGER.info(driver.title)
    assert "OrangeHRM" in driver.title


