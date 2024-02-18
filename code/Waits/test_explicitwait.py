import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import(ElementNotVisibleException,
                                       ElementNotSelectableException)
import os
from dotenv import load_dotenv

def test_login():
    driver = webdriver.Chrome()
    load_dotenv()
    driver.get("https:/app.vwo.com")
    user_name = driver.find_element(By.ID, "login-username")
    password = driver.find_element(By.ID, "login-password")
    btn = driver.find_element(By.ID, "js-login-btn")
    user_name.send_keys(os.getenv("EMAIL"))
    password.send_keys(os.getenv("PASSWORD"))
    btn.click()
    #Fluent Wait
    ignore_list = [ElementNotVisibleException,ElementNotSelectableException]
    wait = WebDriverWait(driver,10,poll_frequency=1,ignored_exceptions=ignore_list)
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".page-heading")))
    #Explicit Wait
    # WebDriverWait(driver,10).until(
    #     EC.text_to_be_present_in_element((By.XPATH,"//h1[contains(text(),'Dashboard')]"),"Dashboard")
    # )
    heading = driver.find_element(By.XPATH,"//span[@class='Fw(semi-bold) ng-binding']")
    assert heading.text == os.getenv("USERNAME"), "Heading text doesn't match"
    print(driver.title)