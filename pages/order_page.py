from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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
            number = int(order.text[-5:])
            order_number_list.append(number)
        return order_number_list

    def wait_order_in_list(self, number, locator):
        result = self.order_number_list(locator)
        while number not in result:
            result = self.order_number_list(locator)
        return result

    def open_order_modal(self, driver):
        self.click_visible_element(LocatorsOrder.ORDER_FEED_LIST)
