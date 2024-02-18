import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    # heading = driver.find_element(By.XPATH,"//button[contains(text(),'Click for JS Alert')]")
    # heading.click()
    # h1 = driver.find_element(By.XPATH, "//button[contains(text(),'Click for JS Confirm')]")
    # h1.click()
    h2 = driver.find_element(By.XPATH, "//button[contains(text(),'Click for JS Prompt')]")
    h2.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    #alert.dismiss()
    alert.send_keys("Ganesh")
    alert.accept()
    # check = driver.find_element(By.XPATH,"//p[contains(text(),'You successfully clicked an alert')]")
    # assert check.text == "You successfully clicked an alert" , 'not matched'
    # print(check.text)
    time.sleep(3)
