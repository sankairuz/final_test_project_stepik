from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    # поиск и нажатие кнопки Add to card
    def add_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add_to_basket.click()

    def verify_price_name(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE_PRICE).text
        price_end = self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE_VER_PRICE).text
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE_NAME).text
        name_end = self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE_VER_NAME).text
        print(price, price_end, name, name_end)
        return price == price_end and name == name_end

    def success_message_add_to_card(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), 'Сообщение о добавлении в корзину появилось, а не должно'

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Сообщение о добавлении не пропадает'