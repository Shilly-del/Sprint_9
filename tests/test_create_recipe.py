import time

from pages import StartPage, RegPage, SignPage, RecipesPage, CreateRecipePage, CardPage

class TestCreateRecipe:
    def test_create_recipe(self, driver_recipe):

        driver, user, recipe = driver_recipe
        start = StartPage(driver)
        start.wait_load()
        start.click_create_acc()

        reg = RegPage(driver)
        reg.wait_load()
        reg.set_user_info(user.name, user.surname, user.username, user.email, user.password)
        reg.click_create_acc()

        sign = SignPage(driver)
        sign.wait_load()
        sign.set_user_info(user.username, user.password)
        sign.click_sign_in()

        recipes = RecipesPage(driver)
        recipes.wait_load()
        recipes.click_create_recipe()

        rec = CreateRecipePage(driver)
        rec.wait_load()
        rec.set_recipe_data(recipe.title, recipe.ingredient, recipe.amount, recipe.time, recipe.description)
        rec.click_create_recipe()

        card = CardPage(driver)
        time.sleep(2)

        assert card.check_card()
        assert card.get_title() == recipe.title


