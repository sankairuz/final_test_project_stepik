import pytest

from .pages.product_page import ProductPage


# def test_add_to_basket(browser):
#     # добавление в корзину, ответ на вопрос в алерте
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.verify_price_name()
@pytest.mark.parametrize('promo_offer',
                         ["0", "1", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    browser.delete_all_cookies()  # очищает кукис перед новым тестом
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    assert page.verify_price_name(), 'Значения имени и/или цены не совпадают'


@pytest.mark.add_to_card
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.delete_all_cookies()
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.success_message_add_to_card()


@pytest.mark.add_to_card
def test_guest_cant_see_success_mesage(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.delete_all_cookies()
    page = ProductPage(browser, link)
    page.open()
    page.success_message_add_to_card()

@pytest.mark.add_to_card
def test_message_disappeared_after_adding_product_ti_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.delete_all_cookies()
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.success_message_is_disappeared()