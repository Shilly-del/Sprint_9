import allure

from locators import RecipesLoc
from pages.base_page import BasePage


class RecipesPage(BasePage):
  
    @allure.step('Ждём загрузку')
    def wait_load(self):
        self.wait_presence(RecipesLoc.EXIT)

    @allure.step('Проверяем, отображается ли кнопка "Выход"')
    def check_exit(self):
        return self.find_element(RecipesLoc.EXIT)

    @allure.step('Нажимаем "Создать рецепт"')
    def click_create_recipe(self):
        self.click(RecipesLoc.CREATE_RECIPE)
