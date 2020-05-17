from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Empty basket message is not " \
                                                                                  "presented "

    def should_not_be_empty_basket_message(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Empty basket message is " \
                                                                                      "presented, but should not "

    def should_be_products_list(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCTS_LIST_IN_BASKET), "Empty basket message is not " \
                                                                                     "presented "

    def should_not_be_products_list(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_LIST_IN_BASKET), "Empty basket message is " \
                                                                                         "presented, but should not "
