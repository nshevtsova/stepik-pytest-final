from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_ADDED_TO_BASKET_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success:nth-child(1)")
    PRODUCT_NAME_IN_PRODUCT_ADDED_TO_BASKET_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success:nth-child(1)>div>strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info")
    BASKET_PRICE_IN_BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info>div>p>strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")