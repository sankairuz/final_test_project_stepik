from .base_page import BasePage
from .locators import MainPageLocators


# BasePage в скобках указывает на то, что MainPage - его наследник
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)