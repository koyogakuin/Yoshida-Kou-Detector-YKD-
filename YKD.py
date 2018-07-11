# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

# Chromeを操作
driver = webdriver.Chrome()

a = 0
count = 1
num = 0

while(a == 0):
    driver.get("https://shindanmaker.com/808441")
    id = driver.find_element_by_name("u")
    id.clear()
    num = random.randint(0, 300000)
    id.send_keys(str(num))
    login_button = driver.find_element_by_id("shindan_submit")
    login_button.click()

    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "result2"))
    )
    result = driver.find_element_by_class_name("result2")

    print(result.text + "--" + str(count) + "回目")
    count = count + 1

    if(result.text == "ヨシダコウ"):
        a = 1

print("総試行回数---" + str(count) + "回")
print("キーワードは" + str(num))
