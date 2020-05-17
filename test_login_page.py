from pages.login_page import LoginPage
from pages.locators import UsedUrls


def test_guest_should_see_correct_url(browser):
    link = UsedUrls.LOGIN_URL
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_guest_should_see_login_form(browser):
    link = UsedUrls.LOGIN_URL
    page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()                      # открываем страницу
    page.should_be_login_form()          # выполняем метод страницы - переходим на страницу логина


def test_guest_should_see_register_form(browser):
    link = UsedUrls.LOGIN_URL
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()

