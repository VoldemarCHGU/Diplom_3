from data import URLS
from helper import *
from locators.forgot_pass_page_locators import LocatorsForgotPass
from pages.base_page import BasePage


class ForgotPassPage(BasePage):

    def send_email(self):
        email = generate_user_data()['email']
        # element = self.find_element_wait_until()
        self.send_keys(locator=LocatorsForgotPass.EMAIL_INPUT, data=email)
        # self.find_element_wait_until().send_keys(email)

    def click_forgot_pass(self):
        self.click_visible_element(LocatorsForgotPass.FORGOT_PASS_LINK)
        self.wait_until_url_change(URLS.LOGIN)

    def click_reset_password_button(self):
        self.click_visible_element(LocatorsForgotPass.RESET_BUTTON)
        # self.wait_until_url_change(URLS.FORGOT_PASS)

    def go_to_reset_pass_page(self):
        self.go_to_page(URLS.FORGOT_PASS)
        self.send_email()
        self.click_visible_element(LocatorsForgotPass.RESET_BUTTON)

    def find_recomended_indo_reset_password(self):
        return self.find_element_with_text('Введите код из письма', tag='label')

    def click_on_show_password(self):
        self.click_visible_element(LocatorsForgotPass.SHOW_PASS_BUTTON)
