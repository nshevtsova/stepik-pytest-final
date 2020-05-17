from selenium.webdriver.common.by import By

class UsedUrls():
    MAIN_URL = "http://selenium1py.pythonanywhere.com/"
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    PRODUCT_THE_CITY_AND_THE_STARS_95_URL = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the" \
                                            "-stars_95/ "



class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini>.btn-group>a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
    PRODUCTS_LIST_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_REPEAT_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form>.btn.btn-lg.btn-primary")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_ADDED_TO_BASKET_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success:nth-child(1)")
    PRODUCT_NAME_IN_PRODUCT_ADDED_TO_BASKET_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success:nth-child(1)>div>strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info")
    BASKET_PRICE_IN_BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info>div>p>strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")