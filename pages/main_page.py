from .base_page import BasePage
from .locators import MainPageLocators


# BasePage в скобках указывает на то, что MainPage - его наследник
class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login is not presented"
