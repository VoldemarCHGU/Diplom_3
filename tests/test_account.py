import allure

from locators.account_page_locators import LocatorsAccount
from pages.account_page import AccountPage


class TestAccount:

    @allure.title('Тест: переход по клику на «Личный кабинет»')
    def test_account_button(self, driver, user_registration):
        user_data, _ = user_registration

        account = AccountPage(driver)
        account.log_in(user_data)
        account.click_visible_element(LocatorsAccount.ACCOUNT_LINK)
        email = account.get_email()

        assert email == user_data['email']

    @allure.title('Тест: переход в раздел «История заказов»')
    def test_move_to_history_auth_user(self, driver, create_order_after_auth):
        user_data = create_order_after_auth['user_data']
        api_order_number = create_order_after_auth['number']

        account = AccountPage(driver)
        account.log_in(user_data)
        account.go_to_profile()
        account.click_order_history_button()

        ui_order_number = account.get_order_number(LocatorsAccount.ORDER_NUMBER_HISTORY)
        assert api_order_number == ui_order_number

    @allure.title('Тест: выход из аккаунта')
    def test_logout(self, driver, authorized_user):
        account = authorized_user
        account.click_logout_button()
        assert account.check_login_form()
