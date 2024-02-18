from selenium import webdriver
from selenium.webdriver.common.by import By


def test_dynamictable():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable1.html")
    table = driver.find_element(By.XPATH,"//table[@summary='Sample Table']/tbody")
    #1 way to get rwos once you find table
    rows = table.find_elements(By.TAG_NAME,"tr") #find element chaining( tr should be within the table)

    for row in rows:
        cols = row.find_elements(By.TAG_NAME,"td")
        for cell in cols:
            print(cell.text)

    #2nd way to get rows once you find table
    # rows = driver.find_element(By.XPATH,"//table[@summary='Sample Table']/tbody/tr")
    # col =driver.find_element(By.XPATH,"//table[@summary='Sample Table']/tbody/tr[1]/td")
    # print(table.text)