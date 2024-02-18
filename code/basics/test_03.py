import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import pytest



def test_cure_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(3)
    # btn = driver.find_elements(By.CLASS_NAME,"btn.btn-dark.btn-lg")
    # btn[0].click()
    # btn = driver.find_elements(By.TAG_NAME,"a")
    # btn[5].click()
    driver.maximize_window()
    appoint_btn = driver.find_element(By.PARTIAL_LINK_TEXT,"Appointment")
    appoint_btn.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", 'url not matching'
    username_ele = driver.find_element(By.NAME,"username")
    username_ele.send_keys("John Doe")
    password_ele = driver.find_element(By.NAME,"password")
    password_ele.send_keys("ThisIsNotAPassword")
    login_btn = driver.find_element(By.ID,"btn-login")
    login_btn.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment", 'Error url'
    logging.info(driver.title)
    time.sleep(5)