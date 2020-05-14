from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to Basket button is not presented"

    def add_to_basket(self):
        button = self.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_add_to_basket_success_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET_SUCCESS_MESSAGE), "Success message is not presented"

    def should_be_added_product_name_correct(self):
        assert self.get_element_text(*ProductPageLocators.PRODUCT_NAME_IN_PRODUCT_ADDED_TO_BASKET_SUCCESS_MESSAGE) \
               == self.get_element_text(*ProductPageLocators.PRODUCT_NAME), "Product name in message is wrong"

    def should_be_basket_price_message(self):
        assert self. is_element_present(*ProductPageLocators.BASKET_PRICE_MESSAGE), "Basket price message is not presented"

    def should_be_added_product_price_correct(self):
        assert self.get_element_text(*ProductPageLocators.BASKET_PRICE_IN_BASKET_PRICE_MESSAGE) \
               == self.get_element_text(*ProductPageLocators.PRODUCT_PRICE), "Product price in message is wrong"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET_SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET_SUCCESS_MESSAGE), \
            "Success message is still presented, but should disappear"
