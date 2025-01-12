import pytest
import requests


class TestDeleteCourier:
    def test_delete_courier(self,api_client):
        response = api_client.delete_courier(id = 444043)
        assert response.status_code == 200
