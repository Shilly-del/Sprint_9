from constants import Url
from pages import StartPage, RegPage, SignPage

class TestCreateAcc:
    def test_create_acc(self, driver):

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

        assert sign.check_url() == Url.SIGN_IN
        assert sign.check_auth_form()


