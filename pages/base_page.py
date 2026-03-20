from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def wait_presence(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))

    def wait_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    def check_url(self):
        return self.driver.current_url

    def load_file(self, locator, path):
        file_input = self.find_element(locator)
        file_input.send_keys(str(path))





