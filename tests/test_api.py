import pytest
import requests
import allure

from Sprint_7.constants import *


class TestDeleteCourier:
    @allure.title("Удаление курьера")
    def test_delete_courier(self, api_client, create_courier_with_id):
        response = api_client.delete_courier(id = create_courier_with_id["id"])
        assert response.status_code == 200

class TestLoginCourier:

    @allure.title("Логин курьера")
    def test_login_courier(self, api_client):
        courier_data = api_client.register_new_courier_and_return_login_password()
        response = api_client.login_courier(data={"login": courier_data[0],"password": courier_data[1],"firstName": courier_data[2]})
        assert response.status_code == 200

    @allure.title("Повторный логин курьера с одинаковыми данными")
    def test_login_courier_with_exist_login(self, api_client, create_courier_with_id):
        response = api_client.create_courier(data={
            "login": create_courier_with_id["login"],
            "password": create_courier_with_id["password"],
            "firstName": create_courier_with_id["first_name"]
        })
        assert response.status_code == 409

    @allure.title("Логин курьера без поля 'логин'")
    def test_login_courier_without_login(self, api_client):
        response = api_client.create_courier(data={
            "login": None,
            "password": "password",
            "firstName": "first_name"
        })
        assert response.status_code == 400

    @allure.title("'id' содержится в тексте ответа при логине курьера")
    def test_login_courier_body_have_id(self, api_client):
        courier_data = api_client.register_new_courier_and_return_login_password()
        response = api_client.login_courier(data={"login": courier_data[0],"password": courier_data[1],"firstName": courier_data[2]})
        assert ID_ASSERTION_TEXT in response.json()

class TestCreateCourier:

    @allure.title("Код ответа при успешном создании курьера")
    def test_create_courier(self,api_client):
        courier_data = api_client.courier_data_for_create()
        response = api_client.create_courier(data={"login": courier_data[0],"password": courier_data[1],"firstName": courier_data[2]})
        assert response.status_code == 201

    @allure.title("Повторное создание курьера")
    def test_create_clone_courier(self,api_client):
        courier_data = api_client.courier_data_for_create()
        api_client.create_courier(data={"login": courier_data[0], "password": courier_data[1], "firstName": courier_data[2]})
        response = api_client.create_courier(data={"login": courier_data[0], "password": courier_data[1], "firstName": courier_data[2]})
        assert response.status_code == 409

    @allure.title("Код ответа при отсутствии логина при создании курьера")
    def test_create_couirier_without_login(self,api_client):
        courier_data = api_client.courier_data_for_create()
        response = api_client.create_courier(
            data={"login": None, "password": courier_data[1], "firstName": courier_data[2]})
        assert response.status_code == 400

    @allure.title("Код ответа при отсутствии пароля при создании курьера")
    def test_create_couirier_without_password(self,api_client):
        courier_data = api_client.courier_data_for_create()
        response = api_client.create_courier(
            data={"login": courier_data[0], "password": None, "firstName": courier_data[2]})
        assert response.status_code == 400

    @allure.title("Тело ответа при успешном создании курьера")
    def test_body_create_courier(self,api_client):
        courier_data = api_client.courier_data_for_create()
        response = api_client.create_courier(
            data={"login": courier_data[0], "password": courier_data[1], "firstName": courier_data[2]})
        assert response.json() == ASSERTION_VALUE_TEST_CREATE_COURIER

    @allure.title("Тело ответа при дублировании данных при создании курьера")
    def test_warning_create_clone_courier(self, api_client):
        courier_data = api_client.courier_data_for_create()
        api_client.create_courier(
            data={"login": courier_data[0], "password": courier_data[1], "firstName": courier_data[2]})
        response = api_client.create_courier(
            data={"login": courier_data[0], "password": courier_data[1], "firstName": courier_data[2]})
        assert TEXT_LOGIN_USED == response.json()

class TestCreateOrder:
    @allure.title("Создание заказа")
    @pytest.mark.parametrize("data",ORDERS_DATA)
    def test_create_order_scooter(self,api_client,data):
        response = api_client.create_order(data= data)
        assert TRACK in response.json()


class TestCourierOrders:
    @allure.title("Получение списка заказов")
    def test_get_courier_orders(self, api_client, create_courier_with_id):
        response = api_client.get_courier_orders(
            params={"courierId": create_courier_with_id["id"],"nearestStation": 2})
        assert isinstance(response.json()["orders"], list)



