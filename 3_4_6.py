from selenium import webdriver
from selenium.webdriver.common.by import By

count = 0

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/3/3.html")
    nums = browser.find_elements(By.TAG_NAME, "p")
    for n in nums:
        count += int(n.text)

print(count)
