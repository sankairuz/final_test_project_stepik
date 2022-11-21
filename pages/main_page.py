from selenium.webdriver.common.by import By

from .base_page import BasePage


class MainPage(BasePage):  # BasePage в скобках указывает на то, что MainPage - его наследник
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, '#login_link')
        login_link.click()

    def should_be_login_link(self):
        self.is_element_present(By.CSS_SELECTOR, '#login_link'), "Login is not presented"