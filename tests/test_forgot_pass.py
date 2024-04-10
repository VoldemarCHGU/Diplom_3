import allure

from data import URLS
from pages.forgot_password_page import ForgotPassPage


class TestForgotPass:

    @allure.title('Тест: переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_forgot_pass_button(self, driver):
        forgot_pass = ForgotPassPage(driver)
        forgot_pass.go_to_page(URLS.LOGIN)
        forgot_pass.click_forgot_pass()

        text_presence = bool(forgot_pass.find_element_with_text('Восстановление пароля'))
        assert text_presence

    @allure.title('Тест: ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email_click_reset(self, driver):
        forgot_page = ForgotPassPage(driver)
        forgot_page.go_to_page(URLS.FORGOT_PASS)
        forgot_page.send_email()
        forgot_page.click_reset_password_button()

        check_text = forgot_page.find_recomended_indo_reset_password()
        assert check_text

    @allure.title('Тест: клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_show_pass_active_input(self, driver):
        forgot_page = ForgotPassPage(driver)
        forgot_page.go_to_reset_pass_page()
        pass_input = self.find_forgot_pass_input()
        forgot_page.click_on_show_password()
        assert 'input_status_active' in pass_input.get_attribute('class')
