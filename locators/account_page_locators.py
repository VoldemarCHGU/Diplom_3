from selenium.webdriver.common.by import By


class LocatorsAccount:
    ACCOUNT_LINK = (By.XPATH, './/a[@href="/account"]')
    ACCOUNT_EMAIL = (By.XPATH, './/label[text()="Логин"]/parent::div/input[@value]')

    ORDER_HISTORY_BUTTON = (By.XPATH, './/a[@href="/account/order-history"]')

    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')
    LOGIN_FORM = ('xpath', '//h2[text()="Вход"]')
    EMAIL = (By.XPATH, './/form//label[text()="Email"]/parent::*/input')
    PASSWORD = (By.XPATH, './/input[@type="password"]')
    ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')
    LOGOUT_BUTTON = (By.XPATH, './/button[text()="Выход"]')
    ORDER_NUMBER_HISTORY = (By.XPATH, './/div[contains(@class,"orderHistory")]//p[contains(text(),"#")]')
