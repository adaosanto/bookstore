import pytest
from django.urls import reverse_lazy
from model_bakery import baker
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

@pytest.fixture
def get_user_token(db):
    user = baker.make(User)
    user.set_password('api@testing')
    token, created = Token.objects.get_or_create(user=user)

    return token

@pytest.fixture
def anonymous_client():
    return APIClient()

@pytest.fixture
def logged_client(get_user_token):
    api_client = APIClient()
    api_client.credentials(HTTP_AUTHORIZATION='Token ' + get_user_token.key)
    return api_client

@pytest.fixture
def data_json_user_create():
    return {
        "first_name": "API",
        "last_name": "Client",
        "username": "api.testing",
        "email": "api@example.com",
        "password": "api@testing",
    }

@pytest.fixture
def data_json_user_patch():
    return {
        "last_name": "PATCH"
    }
@pytest.fixture
def data_json_user_put(data_json_user_create):
    data_put = data_json_user_create.copy()
    data_put['last_name'] = 'PUT'
    
    return data_put



@pytest.mark.django_db
class TestUserCreateView:
    def test_create_new_user(self, anonymous_client: APIClient, data_json_user_create: dict):
        response = anonymous_client.post(
            reverse_lazy("user-create-view"),
            data=data_json_user_create
        )

        assert response.status_code == 201

@pytest.mark.django_db
class TestUserUpdateView:
    def test_update_profile_patch(self, logged_client: APIClient, data_json_user_patch: dict):
        response = logged_client.patch(
            reverse_lazy('user-update-view'),
            data=data_json_user_patch
        )

        assert response.json()['last_name'] == data_json_user_patch['last_name']

    def test_update_profile_put(self, logged_client: APIClient, data_json_user_put: dict):
        response = logged_client.put(
            reverse_lazy('user-update-view'),
            data=data_json_user_put
        )

        assert response.json()['last_name'] == data_json_user_put['last_name']