import allure

from locators import RegLoc
from pages.base_page import BasePage


class RegPage(BasePage):

    @allure.step('Ждём загрузку')
    def wait_load(self):
        self.wait_presence(RegLoc.CREATE_ACC)

    @allure.step('Заполняем поле "Имя"')
    def set_name(self, name):
        self.find_element(RegLoc.NAME).send_keys(name)

    @allure.step('Заполняем поле "Фамилия"')
    def set_surname(self, surname):
        self.find_element(RegLoc.SURNAME).send_keys(surname)

    @allure.step('Заполняем поле "Имя пользователя"')
    def set_username(self, username):
        self.find_element(RegLoc.USERNAME).send_keys(username)

    @allure.step('Заполняем поле "Адрес электронной почты"')
    def set_email(self, email):
        self.find_element(RegLoc.EMAIL).send_keys(email)

    @allure.step('Заполняем поле "Пароль"')
    def set_password(self, password):
        self.find_element(RegLoc.PASSWORD).send_keys(password)

    @allure.step('Заполняем форму регистрации')
    def set_user_info(self, name, surname, username, email, password):
        self.set_name(name)
        self.set_surname(surname)
        self.set_username(username)
        self.set_email(email)
        self.set_password(password)

    @allure.step('Нажимаем "Создать аккаунт')
    def click_create_acc(self):
        self.wait_clickable(RegLoc.CREATE_ACC)
        self.click(RegLoc.CREATE_ACC)