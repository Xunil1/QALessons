from selenium import webdriver


class SeleniumWorker:
    def __init__(self):
        self.driver = None

    def __enter__(self):
        self.driver = webdriver.Chrome()
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.driver is not None:
            self.driver.quit()



