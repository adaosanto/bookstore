from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .models import Publisher
from .serializers import PublisherModelSerializer


class PublisherCreateListView(ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherModelSerializer


class PublisherRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherModelSerializer
