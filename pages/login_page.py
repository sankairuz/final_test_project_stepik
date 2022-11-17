from .base_page import BasePage
from .locators import MainPageLocator, LoginPageLocator


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.curent_url, 'Ссылка не соответствует стандарту'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert LoginPageLocator.LOGIN_FORM != None, 'Отсутствует форма логина'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert LoginPageLocator.REGISTRATION_FORM != None, 'Отсутствует форма регистрации'