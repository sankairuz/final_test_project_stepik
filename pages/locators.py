from selenium.webdriver.common.by import By

class MainPageLocator():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocator():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')