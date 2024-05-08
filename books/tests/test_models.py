from ..models import Book
import pytest
from model_bakery import baker


@pytest.fixture
def book(db):
    return baker.make(Book, title="test")


class TestBookModel:
    def test_str_method(self, book: Book):
        assert str(book) == "Test"
