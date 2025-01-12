import pytest
from Sprint_7.tests.api_client import APIClient  # Убедитесь, что путь корректен

@pytest.fixture
def api_client():
    # Создаём и возвращаем объект APIClient
    return APIClient()
