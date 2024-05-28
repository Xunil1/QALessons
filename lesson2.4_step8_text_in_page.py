import time
import math
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from SeleniumWorker import SeleniumWorker


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

with SeleniumWorker() as browser:
    browser.get(link)

    browser.implicitly_wait(5)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    if price:
        btn = browser.find_element(By.ID, "book")
        btn.click()

        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text
        y = calc(x)

        input_f = browser.find_element(By.ID, "answer")
        input_f.send_keys(str(y))

        btn = browser.find_element(By.ID, "solve")
        btn.click()

        time.sleep(5)