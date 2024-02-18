import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_checkbox():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkbox= driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
    for c in checkbox:
        if not c.is_selected(): #if check box is not selected, it will select
            c.click()
        elif c.is_selected():  #if checkbox is selected, it will untick
            c.click()

    time.sleep(5)


