import time

from selenium.webdriver.common.by import By

from SeleniumWorker import SeleniumWorker


link = "http://suninjuly.github.io/selects1.html"

with SeleniumWorker() as browser:
    browser.get(link)

    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text

    s = int(x) + int(y)

    option = browser.find_element(By.CSS_SELECTOR, f"[value='{s}']").click()

    btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    btn.click()

    time.sleep(10)