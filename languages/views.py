from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .models import Language
from .serializers import LanguageModelSerializer


class LanguageCreateListView(ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageModelSerializer


class LanguageRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageModelSerializer
