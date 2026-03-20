import allure

from constants import Path
from pages.base_page import BasePage
from locators import CreateRecipeLoc


class CreateRecipePage(BasePage):

    @allure.step('Ждём загрузку')
    def wait_load(self):
        self.wait_presence(CreateRecipeLoc.CREATE_RECIPE)

    @allure.step('Заполняем поле "Название рецепта"')
    def set_title(self, title):
        self.find_element(CreateRecipeLoc.TITLE).send_keys(title)

    @allure.step('Заполняем поле "Ингредиенты"')
    def set_ingredient(self, letter):
        '''
        Прописываем первую букву, чтобы открыть список
        '''
        self.find_element(CreateRecipeLoc.INGREDIENTS).send_keys(letter)

    @allure.step('Выбираем ингредиент')
    def click_ingredient(self):
        '''
        добавляем просто первый по списку ингредиент
        '''
        elements = self.wait.until(
        lambda d: d.find_elements(*CreateRecipeLoc.INGREDIENTS_LIST) if len(d.find_elements(*CreateRecipeLoc.INGREDIENTS_LIST)) > 1 else False
    )
        elements[0].click()

    @allure.step('Заполняем поле "Количество"')
    def set_amount(self, amount):
        self.find_element(CreateRecipeLoc.AMOUNT).send_keys(amount)

    @allure.step('Добавляем ингредиент"')
    def add_ingredient(self, ingredient, amount):
        self.set_ingredient(ingredient)
        self.click_ingredient()
        self.set_amount(amount)
        self.click(CreateRecipeLoc.ADD_INGREDIENT)

    @allure.step('Заполняем поле "Время приготовления"')
    def set_time(self, time):
        self.find_element(CreateRecipeLoc.TIME).send_keys(time)

    @allure.step('Заполняем поле "Описание рецепта"')
    def set_description(self, description):
        self.find_element(CreateRecipeLoc.DESCRIPTION).send_keys(description)

    @allure.step('Устанавливаем изображение')
    def set_picture(self):
        self.load_file(CreateRecipeLoc.PICTURE, Path.ASSET)

    @allure.step('Заполняем данные рецепта')
    def set_recipe_data(self, title, ingredient, amount, time, description):
        self.set_title(title)
        self.add_ingredient(ingredient, amount)
        self.set_time(time)
        self.set_description(description)
        self.set_picture()

    @allure.step('Нажимаем "Создать рецепт')
    def click_create_recipe(self):
        self.wait_clickable(CreateRecipeLoc.CREATE_RECIPE)
        self.click(CreateRecipeLoc.CREATE_RECIPE)