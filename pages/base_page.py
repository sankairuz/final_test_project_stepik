import math

from selenium.common.exceptions import NoAlertPresentException  # в начале файла
from selenium.common.exceptions import NoSuchElementException


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
