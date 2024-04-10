from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helper import OrderRequests
from locators.order_page_locators import LocatorsOrder
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    def get_history_orders(self):
        self.wait_element(LocatorsOrder.ORDER_FEED_LIST)
        orders = [element.text.lstrip('#0') for element in
                  self.find_all_elements_wait_until(LocatorsOrder.ORDER_FEED_LIST)]
        return orders

    def wait_order_in_list(self, number):
        if self.check_bool_visability_element(LocatorsOrder.ORDERS_DONE):
            self.wait_until_invisibility_element(LocatorsOrder.ORDERS_DONE)
        LocatorsOrder.NEED_ORDER = number
        number_locator = self.concat_locator_and_number(LocatorsOrder.NEED_ORDER_LIST, number)
        return self.check_bool_visability_element(number_locator)

    def create_order_with_API(self, headers):
        response = OrderRequests.create_order(headers)
        return response.json()['order']['number']

    def click_order_feed(self):
        self.click_visible_element(LocatorsOrder.ORDER_FEED_LIST)

    def check_bool_visability_orders_details(self):
        self.check_bool_visability_element(LocatorsOrder.ORDER_DETAILS)
