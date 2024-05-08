from typing import List

import pytest
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from model_bakery import baker
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from authors.models import Author
from genres.models import Genre
from languages.models import Language
from publishers.models import Publisher

from ..models import Book


@pytest.fixture
def get_user_token(db):
    user = baker.make(User)
    user.set_password("api@testing")
    token, created = Token.objects.get_or_create(user=user)

    return token


@pytest.fixture
def anonymous_client():
    return APIClient()


@pytest.fixture
def logged_client(get_user_token):
    api_client = APIClient()
    api_client.credentials(HTTP_AUTHORIZATION="Token " + get_user_token.key)
    return api_client


@pytest.fixture
def generate_author(db):
    return baker.make(Author)


@pytest.fixture
def generate_genre(db):
    return baker.make(Genre)


@pytest.fixture
def generate_language(db):
    return baker.make(Language)


@pytest.fixture
def generate_publisher(db):
    return baker.make(Publisher)


@pytest.fixture
def generate_list_books(db):
    return baker.make(Book, _quantity=20)


@pytest.fixture
def data_json_book_create(
    generate_author, generate_genre, generate_language, generate_publisher
):
    return {
        "title": "A caminho da felicidade",
        "publication_year": 1985,
        "pages": 325,
        "isbn": "ISBN 9781234567897",
        "description": "API Testing",
        "language": generate_language.id,
        "genre": generate_genre.id,
        "publisher": generate_publisher.id,
        "authors": [generate_author.id],
    }


@pytest.fixture
def data_json_book_put(data_json_book_create):
    data_put = data_json_book_create.copy()
    data_put.update(
        {"pages": 400, "description": "Updated with put", "publication_year": 1966}
    )

    return data_put


@pytest.mark.django_db
class TestBookCreateListView:
    def test_book_create(self, logged_client: APIClient, data_json_book_create: dict):
        response = logged_client.post(
            reverse_lazy("books-create-list"), data=data_json_book_create
        )

        assert response.status_code == 201

    def test_list_book(self, logged_client: APIClient, generate_list_books: List[Book]):
        response = logged_client.get(reverse_lazy("books-create-list"))

        assert response.json()["count"] == len(generate_list_books)

    def test_detail_book(
        self, logged_client: APIClient, generate_list_books: List[Book]
    ):
        first_book = generate_list_books[0]
        response = logged_client.get(
            reverse_lazy("books-detail-view", kwargs={"pk": first_book.id}),
        )
        assert response.json()["title"] == first_book.title

    def test_patch_book(
        self, logged_client: APIClient, generate_list_books: List[Book]
    ):
        first_book = generate_list_books[0]
        data_put = {"title": "patch"}
        response = logged_client.patch(
            reverse_lazy("books-detail-view", kwargs={"pk": first_book.id}),
            data=data_put,
        )
        assert response.status_code == 200

        assert response.json()["title"] == data_put["title"]

    def test_put_book(
        self,
        logged_client: APIClient,
        generate_list_books: List[Book],
        data_json_book_put: dict,
    ):
        first_book = generate_list_books[0]
        response = logged_client.patch(
            reverse_lazy("books-detail-view", kwargs={"pk": first_book.id}),
            data=data_json_book_put,
        )
        assert response.status_code == 200

        assert response.json()["pages"] == data_json_book_put["pages"]
        assert response.json()["description"] == data_json_book_put["description"]
        assert (
            response.json()["publication_year"]
            == data_json_book_put["publication_year"]
        )
