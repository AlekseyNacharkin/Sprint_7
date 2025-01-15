import pytest
import requests
import allure

from Sprint_7.constants import *


class TestDeleteCourier:
    @allure.title("Удаление курьера")
    def test_delete_courier(self, api_client, new_courier):
        response = api_client.delete_courier(id = new_courier["id"])
        assert response.status_code == 200

class TestLoginCourier:

    @allure.title("Авторизация курьера")
    def test_login_courier(self, api_client,new_courier):
        response = api_client.login_courier(data={"login": new_courier["login"],"password": new_courier["password"]})
        assert response.status_code == 200


    @allure.title("Авторизация курьера без поля 'логин'")
    def test_login_courier_without_login(self, api_client):
        response = api_client.login_courier(data={
            "login": None,
            "password": "password"
        })
        assert response.status_code == 400

    @allure.title("Авторизация курьера без поля 'пароль'")
    def test_login_courier_without_password(self, api_client):
        response = api_client.login_courier(data={
            "login": "login",
            "password": ""
        })
        assert response.status_code == 400

    @allure.title("Текст ошибки авторизации не созданного курьера ")
    def test_login_with_uncreated_data(self,api_client):
        response = api_client.login_courier(data={
            "login": "f",
            "password": "d"
        })
        assert response.json().get("message") == ASSERTION_TEXT_AUTHORIZATION

    @allure.title("'id' содержится в тексте ответа при логине курьера")
    def test_login_courier_body_have_id(self, api_client,new_courier):
        response = api_client.login_courier(data={"login": new_courier["login"],"password": new_courier["password"],"firstName": new_courier["first_name"]})
        assert ID_ASSERTION_TEXT in response.json()

class TestCreateCourier:

    @allure.title("Код ответа при успешном создании курьера")
    def test_create_courier(self,api_client,new_courier_data):
        response = api_client.create_courier(data={"login": new_courier_data[0], "password": new_courier_data[1], "firstName": new_courier_data[2]})
        assert response.status_code == 201

    @allure.title("Повторное создание курьера")
    def test_create_clone_courier(self,api_client,new_courier_data):
        api_client.create_courier(data={"login": new_courier_data[0], "password": new_courier_data[1], "firstName": new_courier_data[2]})
        response = api_client.create_courier(data={"login": new_courier_data[0], "password": new_courier_data[1], "firstName": new_courier_data[2]})
        assert response.status_code == 409

    @allure.title("Код ответа при отсутствии логина при создании курьера")
    def test_create_couirier_without_login(self,api_client,new_courier_data):
        response = api_client.create_courier(
            data={"login": None, "password": new_courier_data[1], "firstName": new_courier_data[2]})
        assert response.status_code == 400

    @allure.title("Код ответа при отсутствии пароля при создании курьера")
    def test_create_couirier_without_password(self,api_client,new_courier_data):
        response = api_client.create_courier(
            data={"login": new_courier_data[0], "password": None, "firstName": new_courier_data[2]})
        assert response.status_code == 400

    @allure.title("Тело ответа при успешном создании курьера")
    def test_body_create_courier(self,api_client,new_courier_data):
        response = api_client.create_courier(
            data={"login": new_courier_data[0], "password": new_courier_data[1], "firstName": new_courier_data[2]})
        assert response.json() == ASSERTION_VALUE_TEST_CREATE_COURIER

    @allure.title("Тело ответа при дублировании данных при создании курьера")
    def test_warning_create_clone_courier(self, api_client,new_courier):
        response = api_client.create_courier(
            data={"login": new_courier["login"], "password": new_courier["password"], "firstName": new_courier["first_name"]})
        assert TEXT_LOGIN_USED == response.json()

class TestCreateOrder:
    @allure.title("Создание заказа")
    @pytest.mark.parametrize("data",ORDERS_DATA)
    def test_create_order_scooter(self,api_client,data):
        response = api_client.create_order(data= data)
        assert TRACK in response.json()


class TestCourierOrders:
    @allure.title("Получение списка заказов")
    def test_get_courier_orders(self, api_client, new_courier):
        response = api_client.get_courier_orders(
            params={"courierId": new_courier["id"], "nearestStation": 2})
        assert isinstance(response.json()["orders"], list)



