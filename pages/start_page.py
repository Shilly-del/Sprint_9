import allure

from constants import Url
from locators import StartLoc
from pages.base_page import BasePage


class StartPage(BasePage):

    @allure.step('Открываем стартовую страницу')
    def open_start(self):
        self.open(Url.BASE)
    
    @allure.step('Ждём загрузку')
    def wait_load(self):
        self.wait_presence(StartLoc.CREATE_ACC)

    @allure.step('Нажимаем "Создать аккаунт"')
    def click_create_acc(self):
        self.click(StartLoc.CREATE_ACC)



