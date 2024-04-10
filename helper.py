import random
import string

import allure
import requests

from data import TEST_DATA, API_URL


class RandomUserData:
    def __init__(self):
        self.name = "Vladimir"
        self.email = self.__generate_random_login()
        self.password = self.__generate_random_password_valid()

    def __generate_random_login(self):
        """Генератор логина/почты"""
        random_digit = random.randint(100, 999)
        all_symbols = string.ascii_lowercase
        result = ''.join(random.choice(all_symbols) for _ in range(random.randint(1, 5)))
        email = f"vladimir_nikolaev_diplom_{random_digit}@{result}.com"
        return email

    def __generate_random_password_valid(self):
        """Генератор валидного пароля"""
        all_symbols = string.ascii_letters + string.digits
        result = ''.join(random.choice(all_symbols) for _ in range(random.randint(6, 20)))
        return result

    def get_user_info(self, key=None):
        """для получения данных из класса"""
        data = {"name": self.name, "email": self.email, "password": self.password}
        if key:
            return data[key]
        return {"name": self.name, "email": self.email, "password": self.password}


def generate_user_data():
    user = RandomUserData()
    user_data = user.get_user_info()
    return user_data


class UserRequests:
    @allure.step('Создание нового пользователя (API)')
    def create_user(data):
        return requests.post(API_URL.CREATE_USER, data=data)

    @allure.step(f'Удаление пользователя (API)')
    def delete_request_user(data):
        return requests.delete(API_URL.USER_PATCH_OR_DELETE, headers=data)

    @allure.step('Авторизация пользователя (API)')
    def user_auth(data):
        return requests.post(API_URL.LOGIN_USER, data=data)

    @allure.step(f'Удаление пользователя (API)')
    def delete_user(headers):
        return requests.delete(API_URL.USER_PATCH_OR_DELETE, headers=headers)


class OrderRequests:

    @allure.step(f'Создаём заказ (API)')
    def create_order(headers):
        return requests.post(API_URL.ORDERS, data=TEST_DATA.ingredients, headers=headers)
