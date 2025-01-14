import requests
import requests
import random
import string

class APIClient:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"

    def login_courier(self, endpoint = "/api/v1/courier/login", data=None):
        url = f"{self.BASE_URL}{endpoint}"
        return requests.post(url, json=data)

    def create_courier(self, endpoint = "/api/v1/courier", data=None):
        url = f"{self.BASE_URL}{endpoint}"
        return requests.post(url, json=data)

    def delete_courier(self, endpoint = "/api/v1/courier/", id = None):
        url = f"{self.BASE_URL}{endpoint}{id}"
        return requests.delete(url)

    def create_order(self, endpoint = "/api/v1/orders", data=None):
        url = f"{self.BASE_URL}{endpoint}"
        return requests.post(url, json=data)

    def get_courier_orders(self,endpoint = "/api/v1/orders",params = None):
        url = f"{self.BASE_URL}{endpoint}"
        return requests.get(url,params= params)

    def register_new_courier_and_return_login_password(self):
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # создаём список, чтобы метод мог его вернуть
        login_pass = []

        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = self.create_courier(data=payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        # возвращаем список
        return login_pass

    def courier_data_for_create(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # создаём список, чтобы метод мог его вернуть
        login_pass = []

        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)
        return login_pass
