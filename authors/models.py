from django.db import models

from bookStore.base_models import BaseModel


class Author(BaseModel):
    name = models.CharField("Name", max_length=70, blank=False, unique=True)
