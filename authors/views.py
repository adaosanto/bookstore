from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .models import Author
from .serializers import AuthorModelSerializer


class AuthorCreateListView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class AuthorRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
