import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import URLS
from locators.account_page_locators import LocatorsAccount
from locators.main_page_locators import LocatorsMain
from pages.base_page import BasePage


class AccountPage(BasePage):

    @allure.step('Авторизуемся в вебе')
    def log_in(self, data):
        self.go_to_page(URLS.LOGIN)
        self.send_keys(locator=LocatorsAccount.EMAIL, data=data['email'])
        self.send_keys(locator=LocatorsAccount.PASSWORD, data=data['password'])
        self.click_visible_element(locator=LocatorsAccount.LOGIN_BUTTON)
        self.find_element_wait_until(LocatorsAccount.ORDER_BUTTON)

    def check_login_form(self):
        return self.find_element_wait_until(LocatorsAccount.LOGIN_FORM)

    def click_order_button(self):
        self.click_visible_element(LocatorsAccount.ORDER_BUTTON)

    def click_order_history_button(self):
        self.go_to_page(URLS.ACCOUNT)
        self.click_visible_element(LocatorsAccount.ORDER_HISTORY_BUTTON)

    def get_order_number(self):
        locator = LocatorsAccount.ORDER_NUMBER_HISTORY
        self.wait_hide_text_in_element(locator, '9999')
        web_raw_order_number = self.get_text_element(locator)
        return int(web_raw_order_number[-5:])

    def click_logout_button(self):
        self.click_visible_element(LocatorsAccount.LOGOUT_BUTTON)
        self.wait_until_url_change(URLS.LOGGED_ACCOUNT)

    def get_email(self):
        return self.get_attribute_value(LocatorsAccount.ACCOUNT_EMAIL, 'value')

    def go_to_profile(self):
        self.click_visible_element(LocatorsMain.PROFILE_BTN)

    def get_order_history_number(self):
        return self.get_order_number(LocatorsAccount.ORDER_NUMBER_HISTORY)
