class URLS:
    HOMEPAGE = 'https://stellarburgers.nomoreparties.site'
    LOGIN = f'{HOMEPAGE}/login'
    FORGOT_PASS = f'{HOMEPAGE}/forgot-password'
    ACCOUNT = f'{HOMEPAGE}/account'
    LOGGED_ACCOUNT = f'{ACCOUNT}/profile'
    ORDER_FEED = f'{HOMEPAGE}/feed'


class API_URL:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site/'
    CREATE_USER = f'{MAIN_URL}api/auth/register'
    LOGIN_USER = f'{MAIN_URL}api/auth/login'
    USER_PATCH_OR_DELETE = f'{MAIN_URL}api/auth/user'
    ORDERS = f'{MAIN_URL}api/orders'


class TEST_DATA:
    ingredients = {"ingredients": ["61c0c5a71d1f82001bdaaa71"]}
