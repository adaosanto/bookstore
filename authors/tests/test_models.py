from ..models import Author
import pytest
from model_bakery import baker


@pytest.fixture
def author(db):
    return baker.make(Author, name="test")


class TestAuthorModel:
    def test_str_method(self, author: Author):
        assert str(author) == "Test"
