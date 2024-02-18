import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import logging


def test_login():
    driver = webdriver.Chrome()
    driver.get("https:/app.vwo.com")
    time.sleep(3)
    user_name = driver.find_element(By.ID,"login-username")
    password = driver.find_element(By.ID, "login-password")
    btn = driver.find_element(By.ID, "js-login-btn")
    user_name.send_keys("contact+atb5x@thetestingacademy.com")
    password.send_keys("ATBx@1234")
    btn.click()
    print(driver.title)
    time.sleep(40)
