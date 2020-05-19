from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        currentUrl = self.browser.current_url
        assert currentUrl.find("login") != -1, "Current url does not contain 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_field = self.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        email_field.send_keys(str(email))

        password_field = self.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD)
        password_field.send_keys(str(password))

        repeat_password_field = self.find_element(*LoginPageLocators.REGISTER_REPEAT_PASSWORD_FIELD)
        repeat_password_field.send_keys(str(password))

        register_button = self.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()



