import time
import math
from selenium.webdriver.common.by import By

from SeleniumWorker import SeleniumWorker


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

with SeleniumWorker() as browser:
    browser.get(link)

    btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    btn.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input_f = browser.find_element(By.ID, "answer")
    input_f.send_keys(str(y))

    btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    btn.click()

    alert = browser.switch_to.alert
    print(alert.text)

    time.sleep(5)