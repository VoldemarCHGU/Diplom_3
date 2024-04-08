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
        if driver.command_executor.browser_name == 'chrome':
            ActionChains(driver).click_and_hold(ingredient).move_to_element(burger).release().perform()
        else:
            # Получаем JavaScript код для симуляции перетаскивания
            drag_and_drop_script = """
            var source = arguments[0];
            var target = arguments[1];
            var evt = document.createEvent('UIEvents');
            evt.initUIEvent('dragstart', true, true, window, 1);
            source.dispatchEvent(evt);
            evt = document.createEvent('UIEvents');
            evt.initUIEvent('dragenter', true, true, window, 1);
            target.dispatchEvent(evt);
            evt = document.createEvent('UIEvents');
            evt.initUIEvent('dragover', true, true, window, 1);
            target.dispatchEvent(evt);
            evt = document.createEvent('UIEvents');
            evt.initUIEvent('drop', true, true, window, 1);
            target.dispatchEvent(evt);
            evt = document.createEvent('UIEvents');
            evt.initUIEvent('dragend', true, true, window, 1);
            source.dispatchEvent(evt);
            """
            # Выполняем JavaScript код для симуляции перетаскивания
            driver.execute_script(drag_and_drop_script, ingredient, burger)

    def click_order_button(self):
        self.click_visible_element(LocatorsMain.CREATE_ORDER)

    @allure.step("Закрытие окна с деталями об ингредиенте")
    def close_ingredient_detail_window(self):
        self.click_visible_element(LocatorsMain.MODAL_CLOSE)

    def get_modal_class(self):
        return self.get_attribute_value(LocatorsMain.MODAL, 'class')

    def get_count_ingredients_in_burger(self, count=None):
        return int(self.get_text_element(LocatorsMain.COUNTER))
