from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage):  #BasePage в скобках указывает на то, что MainPage - его наследник
    def go_to_login_page(browser):
        login_link = browser.find_element_by(By.CSS_SELECTOR, '#login_link')
        login_link.click()



