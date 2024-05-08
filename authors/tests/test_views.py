import pytest
from django.urls import reverse_lazy
from model_bakery import baker
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from ..models import Author
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
def generate_list_authors(db):
    return baker.make(Author, _quantity=20)

class TestAuthorCreateListView:
    def test_author_create(self, logged_client: APIClient):
        response = logged_client.post(
            reverse_lazy('authors-create-list'),
            data={'name': 'Person'}
        )

        assert response.status_code == 201

    def test_list_author(self, logged_client: APIClient, generate_list_authors: List[Author]):
        response = logged_client.get(
            reverse_lazy('authors-create-list')
        )
        
        assert response.json()['count'] == len(generate_list_authors)

    def test_detail_author(self, logged_client: APIClient, generate_list_authors: List[Author]):
        first_author = generate_list_authors[0]
        response = logged_client.get(
            reverse_lazy('authors-detail-view', kwargs={'pk': first_author.id}),
        )
        assert response.json()['name'] == first_author.name

    def test_patch_author(self, logged_client: APIClient, generate_list_authors: List[Author]):
        first_author = generate_list_authors[0]
        data_put = {'name': 'patch'}
        response = logged_client.patch(
            reverse_lazy('authors-detail-view', kwargs={'pk': first_author.id}),
            data=data_put
        )
        assert response.status_code == 200

        assert response.json()['name'] == data_put['name']
    
    def test_put_author(self):
        # Not Implemented
        assert True
