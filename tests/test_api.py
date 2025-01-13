import pytest
import requests


class TestDeleteCourier:
    def test_delete_courier(self, api_client, create_courier_with_id):
        response = api_client.delete_courier(id = create_courier_with_id["id"])
        assert response.status_code == 200

class TestLoginCourier:
    def test_login_courier(self, api_client):
        courier_data = api_client.register_new_courier_and_return_login_password()
        response = api_client.login_courier(data={"login": courier_data[0],"password": courier_data[1],"firstName": courier_data[2]})
        assert response.status_code == 200

    def test_login_courier_with_exist_login(self, api_client, create_courier_with_id):
        response = api_client.create_courier_with_id(data={
            "login": create_courier_with_id["login"],
            "password": create_courier_with_id["password"],
            "firstName": create_courier_with_id["first_name"]
        })
        assert response.status_code == 409

    def test_login_courier_without_login(self, api_client):
        response = api_client.create_courier_with_id(data={
            "login": None,
            "password": "password",
            "firstName": "first_name"
        })
        assert response.status_code == 400

    def test_login_courier_body_have_id(self, api_client):
        courier_data = api_client.register_new_courier_and_return_login_password()
        response = api_client.login_courier(data={"login": courier_data[0],"password": courier_data[1],"firstName": courier_data[2]})
        assert "id" in response.json()

class TestCreateCourier:

    def test_create_courier(self,api_client):
        courier_data = api_client.courier_data_for_create()
        response = api_client.create_courier(data={"login": courier_data[0],"password": courier_data[1],"firstName": courier_data[2]})
        assert response.status_code == 201

    def test_create_clone_courier(self,api_client):
        courier_data = api_client.courier_data_for_create()
        api_client.create_courier(data={"login": courier_data[0], "password": courier_data[1], "firstName": courier_data[2]})
        response = api_client.create_courier(data={"login": courier_data[0], "password": courier_data[1], "firstName": courier_data[2]})
        assert response.status_code == 409

    def test_create_couirier_without_login(self,api_client):
        courier_data = api_client.courier_data_for_create()
        response = api_client.create_courier(
            data={"login": None, "password": courier_data[1], "firstName": courier_data[2]})
        assert response.status_code == 400

    def test_create_couirier_without_password(self,api_client):
        courier_data = api_client.courier_data_for_create()
        response = api_client.create_courier(
            data={"login": courier_data[0], "password": None, "firstName": courier_data[2]})
        assert response.status_code == 400

    def test_body_create_courier(self,api_client):
        courier_data = api_client.courier_data_for_create()
        response = api_client.create_courier(
            data={"login": courier_data[0], "password": courier_data[1], "firstName": courier_data[2]})
        assert response.json() == {"ok": True}

    def test_warning_create_clone_courier(self, api_client):
        courier_data = api_client.courier_data_for_create()
        api_client.create_courier(
            data={"login": courier_data[0], "password": courier_data[1], "firstName": courier_data[2]})
        response = api_client.create_courier(
            data={"login": courier_data[0], "password": courier_data[1], "firstName": courier_data[2]})
        assert {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'} == response.json()

###class TestCreateOrder:
    ###"firstName": "Naruto",
    ###"lastName": "Uchiha",
    ###"address": "Konoha, 142 apt.",
    ###"metroStation": 4,
    ###"phone": "+7 800 355 35 35",
    ###"rentTime": 5,
    ###"deliveryDate": "2020-06-06",
    ###"comment": "Saske, come back to Konoha",
    ###"color": [
    ###    "BLACK"
    ###]
###}))
   # def test_color_black_in_order(self,api_client,create_courier_with_id):




