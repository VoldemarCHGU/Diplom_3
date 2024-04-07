import allure
import pytest

from data import URLS
from helper import OrderRequests
from locators.order_page_locators import LocatorsOrder
from pages.order_page import OrderFeedPage


class TestOrder:

    @allure.title('Тест: если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_open_order_modal(self, driver):
        order = OrderFeedPage(driver)

        order.go_to_page(URLS.ORDER_FEED)
        order.click_visible_element(LocatorsOrder.ORDER_FEED_LIST)
        check_modal = order.check_bool_visability_element(LocatorsOrder.ORDER_DETAILS)
        assert check_modal

    @allure.title('Тест: заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_order_in_order_feed(self, driver, authorized_user, create_order_after_auth):
        order = OrderFeedPage(driver)
        authorized_user.click_order_history_button()
        user_order_number = authorized_user.get_order_history_number()
        order.go_to_page(URLS.ORDER_FEED)
        order_list = order.wait_order_in_list(user_order_number, LocatorsOrder.ORDER_FEED_LIST)

        assert user_order_number in order_list

    @allure.title('Тест: счётчики нового заказа "Выполнено за всё время" и "Выполнено за сегодня" увеличиваются')
    @pytest.mark.parametrize('locator', [LocatorsOrder.ALL_TIME_ORDERS, LocatorsOrder.TODAY_ORDERS])
    def test_order_counter_increase(self, driver, user_registration, locator):
        _, headers = user_registration
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.go_to_page(URLS.ORDER_FEED)

        counter_before = int(order_feed_page.get_text_element(locator))
        number = OrderRequests.create_order(headers)
        order_feed_page.wait_order_in_list(number, LocatorsOrder.ORDER_FEED_LIST)
        counter_after = int(order_feed_page.get_text_element(locator))

        assert counter_after > counter_before

    @allure.title('Тест: после оформления заказа его номер появляется в разделе В работе')
    def test_order_in_progress(self, driver, user_registration):
        _, headers = user_registration
        progress = OrderFeedPage(driver)
        progress.go_to_page(URLS.ORDER_FEED)

        number = OrderRequests.create_order(headers)
        order_in_progress = progress.wait_order_in_list(number, LocatorsOrder.ORDER_IN_PROGRESS)
        assert number in order_in_progress
