import pytest
from django.urls import reverse_lazy
from model_bakery import baker
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from ..models import Genre
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
def generate_list_genres(db):
    return baker.make(Genre, _quantity=20)

class TestGenreCreateListView:
    def test_genre_create(self, logged_client: APIClient):
        response = logged_client.post(
            reverse_lazy('genres-create-list'),
            data={'name': 'Person'}
        )

        assert response.status_code == 201

    def test_list_genre(self, logged_client: APIClient, generate_list_genres: List[Genre]):
        response = logged_client.get(
            reverse_lazy('genres-create-list')
        )
        
        assert response.json()['count'] == len(generate_list_genres)

    def test_detail_genre(self, logged_client: APIClient, generate_list_genres: List[Genre]):
        first_genre = generate_list_genres[0]
        response = logged_client.get(
            reverse_lazy('genres-detail-view', kwargs={'pk': first_genre.id}),
        )
        assert response.json()['name'] == first_genre.name

    def test_patch_genre(self, logged_client: APIClient, generate_list_genres: List[Genre]):
        first_genre = generate_list_genres[0]
        data_put = {'name': 'patch'}
        response = logged_client.patch(
            reverse_lazy('genres-detail-view', kwargs={'pk': first_genre.id}),
            data=data_put
        )
        assert response.status_code == 200

        assert response.json()['name'] == data_put['name']
    
    def test_put_genre(self):
        # Not Implemented
        assert True
