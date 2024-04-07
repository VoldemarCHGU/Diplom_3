import allure
import pytest

from data import URLS
from locators.main_page_locators import LocatorsMain
from pages.main_page import MainPage


class TestMain:
    @allure.title('Тест: переход по клику на кнопки «Конструктор» и «Лента заказов»')
    @pytest.mark.parametrize('url, button, header', [
        [URLS.ORDER_FEED, LocatorsMain.CONSTRUCTOR_BUTTON, "Соберите бургер"],
        [URLS.HOMEPAGE, LocatorsMain.ORDER_FEED_BUTTON, "Лента заказов"]])
    def test_click_buttons_in_top(self, driver, url, button, header):
        main_page = MainPage(driver)
        main_page.go_to_page(url)
        main_page.click_visible_element(button)

        header_text = main_page.get_text_element(LocatorsMain.HEADER)
        assert header_text == header

    @allure.title('Тест: если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_open_ingredient_detail(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_page(URLS.HOMEPAGE)
        main_page.click_visible_element(LocatorsMain.INGREDIENT)
        assert main_page.check_bool_visability_element(LocatorsMain.DETAILS_MODAL)

    @allure.title('Тест: всплывающее окно закрывается кликом по крестику')
    def test_close_ingredient_detail(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_page(URLS.HOMEPAGE)
        main_page.open_ingredient_detail_window()
        main_page.close_ingredient_detail_window()

        check_modal = main_page.check_bool_invisability_element(LocatorsMain.MODAL)
        assert not check_modal

    @allure.title('Тест: при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_count_ingredient_after_add(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_page(URLS.HOMEPAGE)

        count_before = main_page.get_count_ingredients_in_burger()
        main_page.move_ingredient_in_burger(driver)
        count_after = main_page.get_count_ingredients_in_burger()

        assert count_after > count_before

    @allure.title('Тест: залогиненный пользователь может оформить заказ.')
    def test_auth_user_create_order(self, driver, authorized_user):
        authorized_user.go_to_page(URLS.HOMEPAGE)
        authorized_user.click_order_button()

        order_number = authorized_user.get_order_number(LocatorsMain.ORDER_NUMBER)
        assert order_number > 0
