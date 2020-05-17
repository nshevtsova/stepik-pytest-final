from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.locators import UsedUrls
import pytest
import time


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()  # stepik quiz for some step

    page.should_be_add_to_basket_success_message()
    page.should_be_added_product_name_correct()

    page.should_be_basket_price_message()
    page.should_be_added_product_price_correct()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = UsedUrls.PRODUCT_THE_CITY_AND_THE_STARS_95_URL
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_can_see_product_in_basket_opened_from_product_page_after_product_adding(browser):
    # additional positive test
    link = UsedUrls.PRODUCT_THE_CITY_AND_THE_STARS_95_URL
    page = ProductPage(browser, link)
    page.open()  # Гость открывает страницу товара
    page.add_to_basket()
    page.go_to_basket()  # Переходит в корзину по кнопке в шапке
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_products_list()  # Ожидаем, что в корзине есть товар
    basket_page.should_not_be_empty_basket_message()  # Ожидаем, что нет текста о том что корзина пуста


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = UsedUrls.PRODUCT_THE_CITY_AND_THE_STARS_95_URL
    page = ProductPage(browser, link)
    page.open()  # Гость открывает страницу товара
    page.go_to_basket()  # Переходит в корзину по кнопке в шапке
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_list()  # Ожидаем, что в корзине нет товаров
    basket_page.should_be_empty_basket_message()  # Ожидаем, что есть текст о том что корзина пуста


def test_guest_cant_see_success_message(browser):
    link = UsedUrls.PRODUCT_THE_CITY_AND_THE_STARS_95_URL
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="by design")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = UsedUrls.PRODUCT_THE_CITY_AND_THE_STARS_95_URL
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = UsedUrls.PRODUCT_THE_CITY_AND_THE_STARS_95_URL
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail(reason="by design")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = UsedUrls.PRODUCT_THE_CITY_AND_THE_STARS_95_URL
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_success_message_disappeared()


@pytest.mark.add_to_basket_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = UsedUrls.LOGIN_URL
        page = LoginPage(browser, link)
        page.open()  # открыть страницу регистрации

        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())

        page.register_new_user(email, password)  # зарегистрировать нового пользователя
        page.should_be_authorized_user()  # проверить, что пользователь залогинен

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = UsedUrls.PRODUCT_THE_CITY_AND_THE_STARS_95_URL
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()

        page.should_be_add_to_basket_success_message()
        page.should_be_added_product_name_correct()

        page.should_be_basket_price_message()
        page.should_be_added_product_price_correct()

    def test_user_cant_see_success_message(self, browser):
        link = UsedUrls.PRODUCT_THE_CITY_AND_THE_STARS_95_URL
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()




