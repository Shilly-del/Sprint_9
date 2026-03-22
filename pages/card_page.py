import allure

from locators import RecipeCardLoc
from pages.base_page import BasePage


class CardPage(BasePage):

    @allure.step('Проверяем отображение карточки созданного рецепта')
    def check_card(self):
        return self.find_element(RecipeCardLoc.CARD)

    @allure.step('Получаем название рецепта')
    def get_title(self):
        return self.find_element(RecipeCardLoc.TITLE).text

    @allure.step('Ждём текст карточки')
    def wait_title(self, title):
        '''
        для воркфлоу, без него слетает тест :(
        '''
        self.wait_text(RecipeCardLoc.TITLE, title)


