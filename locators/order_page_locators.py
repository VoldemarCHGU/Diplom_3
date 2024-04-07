from selenium.webdriver.common.by import By


class LocatorsOrder:
    ORDER_FEED_LIST = (By.XPATH, './/ul[contains(@class,"OrderFeed_list")]//p[contains(text(),"#")]')
    ORDER_DETAILS = (By.XPATH, './/section[contains(@class,"modal_opened")]//ul/li')
    ALL_TIME_ORDERS = (
        By.XPATH, './/p[text()="Выполнено за все время:"]/following::p[contains(@class,"OrderFeed_number")]')
    TODAY_ORDERS = (By.XPATH, './/p[text()="Выполнено за сегодня:"]/following::p[contains(@class,"OrderFeed_number")]')
    ORDER_IN_PROGRESS = (By.XPATH, './/ul[contains(@class,"OrderFeed_orderListReady")]/li')
    ORDERS_DONE = (By.XPATH, '//li[text()="Все текущие заказы готовы!"]')
