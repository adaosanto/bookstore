from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .models import Book
from .serializers import BookModelSerializer


class BookCreateListView(ListCreateAPIView):
    """Visualização para listar e criar livros."""

    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BookRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """Visualização para recuperar, atualizar e excluir um livro."""

    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
