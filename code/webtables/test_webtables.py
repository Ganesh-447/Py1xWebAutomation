import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_webtables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    table_rows = driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr")
    rows = len(table_rows)
    print(f' no of rows are {rows}')
    tabl_col = driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr[2]/td")
    col = len(tabl_col)
    print(f' no of columns are {col}')
    time.sleep(1)

    first_part = "//table[@id='customers']/tbody/tr["
    second_part= "]/td["
    third_part = "]"

    for i in range(2,rows+1):
        for j in range(1,col+1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            #print(dynamic_path)
            data = driver.find_element(By.XPATH,dynamic_path).text
            #print(data,end=" ")
            if "Helen Bennett" in data:
                country_path = f"{dynamic_path}/following-sibling::td"
                country = driver.find_element(By.XPATH,country_path).text
                print(f'Helen Bennett country is {country}')