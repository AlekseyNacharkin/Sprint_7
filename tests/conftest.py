import pytest
from Sprint_7.tests.api_client import APIClient

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_courier_with_id(api_client):
    create_data = api_client.register_new_courier_and_return_login_password()
    id = api_client.login_courier(data={"login":create_data[0],"password":create_data[1]})
    DATA = id.json()
    return {"id":DATA["id"],"login":create_data[0],"password":create_data[1],"first_name":create_data[2]}




