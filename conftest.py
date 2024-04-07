import pytest
from selenium import webdriver

from data import *
from helper import *
from pages.account_page import AccountPage


@pytest.fixture(params=['chrome', 'firefox'])
@allure.title(f'Запуск драйвера')
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    driver.set_window_size(1920, 1080)
    driver.get(URLS.HOMEPAGE)
    yield driver
    driver.quit()


@allure.step('Регистрация пользователя')
@pytest.fixture
def user_registration():
    user_data = generate_user_data()
    response = UserRequests.create_user(data=user_data)
    headers = {'Authorization': response.json()["accessToken"]}
    yield user_data, headers
    UserRequests.delete_user(headers=headers)


@allure.step('Создание заказа (API)')
@pytest.fixture
def create_order_after_auth(user_registration):
    user_data, headers = user_registration
    response_order = OrderRequests.create_order(headers=headers)

    number = response_order.json()['order']['number']
    return {'user_data': user_data, 'number': number}


@allure.step('Переход в аккаунт')
@pytest.fixture
def authorized_user(user_registration, driver):
    user_data, headers = user_registration
    account_page = AccountPage(driver)
    account_page.log_in(user_data)
    account_page.go_to_page(URLS.ACCOUNT)
    return account_page
