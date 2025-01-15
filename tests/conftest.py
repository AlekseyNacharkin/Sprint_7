import pytest
from Sprint_7.tests.api_client import APIClient

@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def new_courier_data(api_client):
    datas = api_client.courier_data_for_create()
    yield datas
    try:
        response = api_client.login_courier(data={"login": datas[0], "password": datas[1]})
        if response.status_code != 200:
            print(f"Ошибка авторизации")
            return
        id_user = response.json()
        code = id_user.get("code")
        if code == 200:
            api_client.delete_courier(id=id_user.get("id"))
        else:
            print(f"Не удалось авторизовать курьера: {id_user}")
    except Exception as e:
        print(f"Ошибка при выполнении teardown: {e}")

@pytest.fixture
def new_courier(api_client):
    create_data = api_client.register_new_courier_and_return_login_password()
    id = api_client.login_courier(data={"login":create_data[0],"password":create_data[1]})
    DATA = id.json()
    yield {"id":DATA["id"],"login":create_data[0],"password":create_data[1],"first_name":create_data[2]}
    api_client.delete_courier(id = DATA["id"])
