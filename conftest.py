import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOption
from selenium.webdriver.firefox.options import Options as FirefoxOption

from data import *
from helper import *
from pages.account_page import AccountPage


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', help="Choose browser: chrome or firefox")
    parser.addoption('--headless', default='true', help='headless options: "true" or "false"')


@pytest.fixture
@allure.title(f'Запуск драйвера')
def driver(request):
    browser = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')

    if browser == 'firefox':
        firefox_option = FirefoxOption()
        if headless == 'true':
            firefox_option.add_argument('--headless')
            firefox_option.add_argument('--ignore-certificate-errors')
        driver = webdriver.Firefox(options=firefox_option)
    elif browser == 'chrome':
        chrome_option = ChromeOption()
        if headless == 'true':
            chrome_option.add_argument('--headless')
        chrome_option.add_argument('--ignore-certificate-errors')
        chrome_option.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=chrome_option)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    request.addfinalizer(lambda *args: driver.quit())
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
