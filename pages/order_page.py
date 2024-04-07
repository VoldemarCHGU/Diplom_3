from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helper import OrderRequests
from locators.order_page_locators import LocatorsOrder
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    def get_history_orders(self):
        self.wait_element(LocatorsOrder.ORDER_FEED_LIST)
        orders = [element.text.lstrip('#0') for element in self.driver.find_elements(LocatorsOrder.ORDER_FEED_LIST)]
        return orders

    def order_number_list(self, locator):
        order_list = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        order_number_list = []
        for order in order_list:
            number = int(order.text[1:])
            order_number_list.append(number)
        return order_number_list

    def wait_order_in_list(self, number, locator):
        if self.check_bool_visability_element(LocatorsOrder.ORDERS_DONE):
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(LocatorsOrder.ORDERS_DONE))
        order_list = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        order_number_list = []
        for order in order_list:
            order_number_list.append(int(order.text[1:]))
        return order_number_list

    def open_order_modal(self):
        self.click_visible_element(LocatorsOrder.ORDER_FEED_LIST)

    def create_order_with_API(self, headers):
        response = OrderRequests.create_order(headers)
        return response.json()['order']['number']
