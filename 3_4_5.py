import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/2/2.html")
    browser.find_element(By.PARTIAL_LINK_TEXT, "16243162441624").click()
    time.sleep(100)
