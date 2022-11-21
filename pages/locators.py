from selenium.webdriver.common.by import By


# Этот файл содержит в себе селекторы, каждый класс для каждой страницы

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
