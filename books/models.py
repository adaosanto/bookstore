from django.db import models

from authors.models import Author
from bookStore.base_models import BaseModel
from genres.models import Genre
from languages.models import Language
from publishers.models import Publisher


class Book(BaseModel):
    title = models.CharField("Title", max_length=100, blank=False, unique=True)
    authors = models.ManyToManyField(Author, blank=False)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    publication_year = models.IntegerField("Publication Year", blank=False)
    pages = models.IntegerField("Num of Pages", blank=False)
    isbn = models.CharField(
        "International Standard Book Number", max_length=22, blank=False
    )
    description = models.TextField("Description", blank=False)

    def __str__(self):
        return self.title.capitalize()
