import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from constants import Url
from helper import User, Recipe


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")    
    chrome_options.add_argument("--no-sandbox")   
    chrome_options.add_argument("--disable-dev-shm-usage") 
    chrome_options.add_argument("--window-size=1920,1080")
    with allure.step(f"Создаём пользователя"):
        user = User()
    with allure.step(f"Инициализируем драйвер"):
        driver = webdriver.Chrome(options=chrome_options)
    with allure.step(f"Открываем стартовую страницу"):   
        driver.get(Url.BASE)
    yield driver, user
    with allure.step(f"Закрываем браузер"):
        driver.quit()

@pytest.fixture
def driver_recipe():
    chrome_options = Options()
    chrome_options.add_argument("--headless")     
    chrome_options.add_argument("--no-sandbox")    
    chrome_options.add_argument("--disable-dev-shm-usage") 
    chrome_options.add_argument("--window-size=1920,1080")
    with allure.step(f"Создаём пользователя"):
        user = User()
    with allure.step(f"Создаём данные рецепта"):
        recipe = Recipe()
    with allure.step(f"Инициализируем драйвер"):
        driver = webdriver.Chrome(options=chrome_options)
    with allure.step(f"Открываем стартовую страницу"):   
        driver.get(Url.BASE)
    yield driver, user, recipe
    with allure.step(f"Закрываем браузер"):
        driver.quit()
