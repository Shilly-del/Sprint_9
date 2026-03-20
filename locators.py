from selenium.webdriver.common.by import By

class StartLoc:
    CREATE_ACC = By.XPATH, '//*[contains(@class, "styles_menuButton") and text() = "Создать аккаунт"]'
    SIGN_IN = By.XPATH, '//*[contains(@class, "styles_menuLink") and text() = "Войти"]'

class RegLoc:
    NAME = By.NAME, "first_name"
    SURNAME = By.NAME, "last_name"
    USERNAME = By.NAME, "username"
    EMAIL = By.NAME, "email"
    PASSWORD = By.NAME, "password"
    CREATE_ACC = By.XPATH, '//button[contains(@class, "styles_button") and text() = "Создать аккаунт"]'
    
class SignLoc:
    FORM = By.XPATH, '//form[contains(@class, "styles_form")]'
    EMAIL = By.NAME, "email"
    PASSWORD = By.NAME, "password"
    SIGN_IN = By.XPATH, '//button[contains(@class, "styles_button") and text() = "Войти"]'

class RecipesLoc:
    EXIT = By.XPATH, '//*[contains(@class, "styles_menuLink") and text() = "Выход"]'
    CREATE_RECIPE = By.XPATH, '//*[contains(@class, "style_nav__link") and text() = "Создать рецепт"]'

class CreateRecipeLoc:
    TITLE = By.XPATH, '//*[contains(text(), "Название рецепта")]/following-sibling::input[contains(@class, "styles_inputField")]'
    INGREDIENTS = By.XPATH, '//input[contains(@class, "styles_ingredientsInput")]'
    INGREDIENTS_LIST = By.XPATH, '//div[contains(@class, "styles_container")]/div'
    AMOUNT = By.XPATH, '//input[contains(@class, "styles_ingredientsAmountValue")]'
    ADD_INGREDIENT = By.XPATH, '//*[contains(@class, "styles_ingredientAdd") and text() = "Добавить ингредиент"]'
    TIME = By.XPATH, '//*[contains(text(), "Время приготовления")]/following-sibling::input[contains(@class, "styles_inputField")]'
    PICTURE = By.XPATH, '//input[contains(@class, "styles_fileInput") and @type = "file"]'
    DESCRIPTION = By.XPATH, '//*[contains(text(), "Описание рецепта")]/following-sibling::textarea[contains(@class, "styles_textareaField")]'
    CREATE_RECIPE = By.XPATH, '//button[contains(@class, "style_button") and text() = "Создать рецепт"]'

class RecipeCardLoc:
    CARD = By.XPATH, '//div[contains(@class, "styles_single-card")]/img'
    TITLE = By.XPATH, '//*[contains(@class, "styles_single-card__title")]'