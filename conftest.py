import allure
import pytest

from selenium import webdriver

from constants import Url
from helper import User, Recipe


@pytest.fixture
def driver():
    with allure.step(f"Создаём пользователя"):
        user = User()
    with allure.step(f"Инициализируем драйвер"):
        driver = webdriver.Chrome()
    with allure.step(f"Открываем стартовую страницу"):   
        driver.get(Url.BASE)
    yield driver, user
    with allure.step(f"Закрываем браузер"):
        driver.quit()

@pytest.fixture
def driver_recipe():
    with allure.step(f"Создаём пользователя"):
        user = User()
    with allure.step(f"Создаём данные рецепта"):
        recipe = Recipe()
    with allure.step(f"Инициализируем драйвер"):
        driver = webdriver.Chrome()
    with allure.step(f"Открываем стартовую страницу"):   
        driver.get(Url.BASE)
    yield driver, user, recipe
    with allure.step(f"Закрываем браузер"):
        driver.quit()
