from selenium.webdriver.common.by import By


class LocatorsForgotPass:
    FORGOT_PASS_LINK = (By.XPATH, './/a[@href="/forgot-password"]')
    SHOW_PASS_BUTTON = (By.XPATH, './/form//label[text()="Пароль"]//following::*[local-name()="svg"]')
    PASS_INPUT = (By.XPATH, './/div[contains(@class,"input_type_password")]')
    EMAIL_INPUT = (By.XPATH, './/form//label[text()="Email"]/parent::*/input')
    RESET_BUTTON = (By.XPATH, './/form//button[text()="Восстановить"]')
