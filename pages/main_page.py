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
        ActionChains(driver).drag_and_drop(ingredient, burger).perform()

    def click_order_button(self):
        self.click_visible_element(LocatorsMain.CREATE_ORDER)

    @allure.step("Закрытие окна с деталями об ингредиенте")
    def close_ingredient_detail_window(self):
        self.click_visible_element(LocatorsMain.MODAL_CLOSE)

    def get_modal_class(self):
        return self.get_attribute_value(LocatorsMain.MODAL, 'class')

    def get_count_ingredients_in_burger(self):
        return int(self.get_text_element(LocatorsMain.COUNTER))
