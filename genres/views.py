from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .models import Genre
from .serializers import GenreModelSerializer


class GenreCreateListView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer


class GenreRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer
