from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.locators import UsedUrls
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = UsedUrls.MAIN_URL
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
        page.open()                      # открываем страницу
        page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = UsedUrls.MAIN_URL
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_should_see_correct_url(browser):
    link = UsedUrls.MAIN_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()


def test_guest_should_see_login_form(browser):
    link = UsedUrls.MAIN_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_form()          # выполняем метод страницы - переходим на страницу логина


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = UsedUrls.MAIN_URL
    page = MainPage(browser, link)
    page.open()  # Гость открывает главную страницу
    page.go_to_basket()  # Переходит в корзину по кнопке в шапке сайта
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_list()  # Ожидаем, что в корзине нет товаров
    basket_page.should_be_empty_basket_message()  # Ожидаем, что есть текст о том что корзина пуста


def test_guest_should_see_register_form(browser):
    link = UsedUrls.MAIN_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_register_form()
