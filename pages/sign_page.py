import allure

from locators import SignLoc
from pages.base_page import BasePage

class SignPage(BasePage):

    @allure.step('Ждём загрузку')
    def wait_load(self):
        self.find_element(SignLoc.SIGN_IN)

    @allure.step('Проверяем, что форма авторизации присутствует на странице')
    def check_auth_form(self):
        return self.find_element(SignLoc.FORM)

    @allure.step('Заполняем поле "Адрес электронной почты"')
    def set_email(self, email):
        self.find_element(SignLoc.EMAIL).send_keys(email)

    @allure.step('Заполняем поле "Пароль"')
    def set_password(self, password):
        self.find_element(SignLoc.PASSWORD).send_keys(password)

    @allure.step('Заполняем форму авторизации')
    def set_user_info(self, email, password):
        self.set_email(email)
        self.set_password(password)

    @allure.step('Нажимаем "Войти')
    def click_sign_in(self):
        self.wait_clickable(SignLoc.SIGN_IN)
        self.click(SignLoc.SIGN_IN)

