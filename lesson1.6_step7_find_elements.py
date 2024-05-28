import time
import math

from selenium.webdriver.common.by import By

from SeleniumWorker import SeleniumWorker

link = "http://suninjuly.github.io/huge_form.html"

with SeleniumWorker() as browser:
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(10)
