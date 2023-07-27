import pytest
from django.test import Client
from django.contrib.auth.models import User

@pytest.fixture
def test_client() -> Client:
    return  Client()

@pytest.fixture
def authenticated_client(test_client) -> tuple[Client, User]:
    user = User.objects.create_user("Test", "test@test.com", "testpassword")

    test_client.force_login(user)
    return test_client, user
