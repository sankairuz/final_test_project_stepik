from selenium.webdriver.common.by import By


# Этот файл содержит в себе селекторы, каждый класс для каждой страницы

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    GO_TO_BASKET = (By.CSS_SELECTOR, 'span a.btn-default.btn')
    PRODUCT_PAGE_NAME = (By.CSS_SELECTOR, '.col-sm-6 h1')
    PRODUCT_PAGE_PRICE = (By.CSS_SELECTOR, '.col-sm-6 .price_color')
    PRODUCT_PAGE_VER_NAME = (By.CSS_SELECTOR, '.alertinner strong')
    PRODUCT_PAGE_VER_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
