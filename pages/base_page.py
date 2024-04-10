from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def concat_locator_and_number(locator, value):
        method, locator = locator
        return method, locator.format(value)

    def current_url(self):
        return self.driver.current_url

    def go_to_page(self, url):
        self.driver.get(url)

    def find_element_wait_until(self, locator, time=30):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_all_elements_wait_until(self, locator, time=30):
        WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator))
        return self.driver.find_element(*locator)

    def find_element_with_text(self, text, tag='*'):
        return self.find_element_wait_until((By.XPATH, f'.//{tag}[text()="{text}"]'))

    def check_bool_visability_element(self, locator):
        return bool(self.find_element_wait_until(locator))

    def check_bool_until_not_invisability_element(self, locator):
        return bool(WebDriverWait(self.driver, 10).until_not(EC.visibility_of_element_located(locator)))

    def wait_until_invisibility_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))

    def wait_hide_text_in_element(self, locator, text):
        WebDriverWait(self.driver, 20).until_not(EC.text_to_be_present_in_element(locator, text))

    def send_keys(self, locator, data):
        self.find_element_wait_until(locator).send_keys(data)

    def click_visible_element(self, locator, time=10):
        # Выполняем клик с помощью ActionChains (стабильность для firefox)
        action = ActionChains(self.driver)
        element = self.find_element_wait_until(locator, time)
        action.move_to_element(element).click().perform()

    def wait_until_url_change(self, url):
        WebDriverWait(self.driver, 5).until(EC.url_changes(url))

    def get_text_element(self, locator):
        return self.find_element_wait_until(locator).text

    def get_attribute_value(self, locator, attribute):
        return self.find_element_wait_until(locator).get_attribute(attribute)
