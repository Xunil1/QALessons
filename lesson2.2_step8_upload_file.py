import time
import os
from selenium.webdriver.common.by import By

from SeleniumWorker import SeleniumWorker


link = "http://suninjuly.github.io/file_input.html"

with SeleniumWorker() as browser:
    browser.get(link)

    name_input = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    name_input.send_keys("First")

    last_name_input = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last_name_input.send_keys("Last")

    email_input = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email_input.send_keys("Email")

    file_input = browser.find_element(By.CSS_SELECTOR, "input[type='file']")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'send_file.txt')

    file_input.send_keys(file_path)

    btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    btn.click()

    time.sleep(5)