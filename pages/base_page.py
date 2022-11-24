import math

from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, \
    TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators


class BasePage:
    # здесь определяется содержимое класса browser, url и время неявного ожидания
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """
        Функция непосредственного запуска страницы по url
        """
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """
        Определяет, находится ли элемент по заданному селектору
        :param how: - как искать(By.CSS_SELECTOR)
        :param what: - селектор
        :return: - True/False, в зависимости от наличия элемента
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        """
        Заходит в алерт, берёт оттуда значение и выводит на печать
        :return: - возвращае
        """
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):
        """
        Проверка на отсутствие элемента
        :param how: что искать
        :param what: как искать
        :param timeout: время ожидания, по умолчанию 4сек
        :return: True если элемент не найдет, False в противном случае
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """
        Проверка, пропадает ли элемент со временем
        :param how: как искать
        :param what: что искать
        :param timeout: время ожидания, по умолчанию 4сек
        :return: True если элемент со временем пропадает, False в противном случае
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        """ Переход в страницу авторизации """
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        """ Видна ли кнопка Войти """
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket(self):
        """  Переход в корзину """
        self.browser.find_element(*BasePageLocators.BTN_BASKET).click()

    def basket_empty(self):
        """ Пуста ли корзина """
        message = self.browser.find_element(*BasePageLocators.MESSGAGE_BASKET_EMPTY).text
        assert 'Ваша корзина пуста' in message, 'Корзина не пуста'
