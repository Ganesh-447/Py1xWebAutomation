import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.keys import Keys


def test_action_chain():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    # create an object
    actions = ActionChains(driver)
    name = driver.find_element(By.NAME,"firstname")
    actions.key_down(Keys.SHIFT).send_keys_to_element(name,"ganesh")\
    .key_up(Keys.SHIFT).perform()
    time.sleep(3)
    # action = ActionBuilder(driver)
    # actions.dr
