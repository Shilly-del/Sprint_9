from constants import Url
from pages import StartPage, RegPage, SignPage, RecipesPage

class TestSignIn:
    def test_sign_in(self, driver):

        driver, user = driver
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

        assert recipes.check_url() == Url.RECIPES
        assert recipes.check_exit()


