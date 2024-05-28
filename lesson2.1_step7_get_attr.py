import time
import math

from selenium.webdriver.common.by import By

from SeleniumWorker import SeleniumWorker


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

with SeleniumWorker() as browser:
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    x = int(x_element.get_attribute("valuex"))
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(str(y))

    chkbox = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox'")
    chkbox.click()

    rbtn_lbl = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    rbtn_lbl.click()

    btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    btn.click()

    time.sleep(5)