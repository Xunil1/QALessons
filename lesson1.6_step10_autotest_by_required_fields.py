import time

from selenium.webdriver.common.by import By

from SeleniumWorker import SeleniumWorker

link = "http://suninjuly.github.io/registration1.html"
#link = "https://suninjuly.github.io/registration2.html"

with SeleniumWorker() as browser:
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_input = browser.find_element(By.XPATH, "//input[contains(@class, 'first') and @required]")
    first_input.send_keys("Тест")
    second_input = browser.find_element(By.XPATH, "//input[contains(@class, 'second') and @required]")
    second_input.send_keys("Тест")
    third_input = browser.find_element(By.XPATH, "//input[contains(@class, 'third') and @required]")
    third_input.send_keys("Тест")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    time.sleep(5)