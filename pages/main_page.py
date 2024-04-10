import allure
from selenium.webdriver import ActionChains

from locators.main_page_locators import LocatorsMain
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Просмотр деталей ингредиента")
    def open_ingredient_detail_window(self):
        self.click_visible_element(LocatorsMain.INGREDIENT)

    def move_ingredient_in_burger(self, driver):
        burger = self.find_element_wait_until(LocatorsMain.BURGER)
        ingredient = self.find_element_wait_until(LocatorsMain.INGREDIENT)
        # на хром перетаскивается, на firefox решения не нашёл пока что нормального
        if self.get_browser_name(driver) == 'chrome':
            self.click_and_hold_move_to_element_chrome(driver, what=ingredient, where=burger)
        else:
            self.driver_execute_script_move_for_firefox(driver, what=ingredient, where=burger)

    def click_order_button(self):
        self.click_visible_element(LocatorsMain.CREATE_ORDER)

    def click_ingredient(self):
        self.click_visible_element(LocatorsMain.INGREDIENT)

    @allure.step("Закрытие окна с деталями об ингредиенте")
    def close_ingredient_detail_window(self):
        self.click_visible_element(LocatorsMain.MODAL_CLOSE)

    def get_modal_class(self):
        return self.get_attribute_value(LocatorsMain.MODAL, 'class')

    def get_count_ingredients_in_burger(self, count=None):
        return int(self.get_text_element(LocatorsMain.COUNTER))

    def get_text_in_header(self):
        return self.get_text_element(LocatorsMain.HEADER)

    def check_close_modal_window(self):
        self.check_bool_until_not_invisability_element(LocatorsMain.MODAL)

    def check_details_modal_window(self):
        self.check_bool_visability_element(LocatorsMain.DETAILS_MODAL)
