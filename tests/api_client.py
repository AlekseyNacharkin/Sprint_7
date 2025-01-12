import requests

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
