import pytest
from django.urls import reverse_lazy
from model_bakery import baker
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from ..models import Publisher
from typing import List

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
def generate_list_publishers(db):
    return baker.make(Publisher, _quantity=20)

class TestPublisherCreateListView:
    def test_publisher_create(self, logged_client: APIClient):
        response = logged_client.post(
            reverse_lazy('publishers-create-list'),
            data={'name': 'Person'}
        )

        assert response.status_code == 201

    def test_list_publisher(self, logged_client: APIClient, generate_list_publishers: List[Publisher]):
        response = logged_client.get(
            reverse_lazy('publishers-create-list')
        )
        
        assert response.json()['count'] == len(generate_list_publishers)

    def test_detail_publisher(self, logged_client: APIClient, generate_list_publishers: List[Publisher]):
        first_publisher = generate_list_publishers[0]
        response = logged_client.get(
            reverse_lazy('publishers-detail-view', kwargs={'pk': first_publisher.id}),
        )
        assert response.json()['name'] == first_publisher.name

    def test_patch_publisher(self, logged_client: APIClient, generate_list_publishers: List[Publisher]):
        first_publisher = generate_list_publishers[0]
        data_put = {'name': 'patch'}
        response = logged_client.patch(
            reverse_lazy('publishers-detail-view', kwargs={'pk': first_publisher.id}),
            data=data_put
        )
        assert response.status_code == 200

        assert response.json()['name'] == data_put['name']
    
    def test_put_publisher(self):
        # Not Implemented
        assert True
