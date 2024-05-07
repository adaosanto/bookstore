from django.urls import path

from .views import PublisherCreateListView, PublisherRetrieveUpdateDestroyView

urlpatterns = [
    path(
        "publishers/", PublisherCreateListView.as_view(), name="publishers-create-list"
    ),
    path(
        "publishers/<int:pk>",
        PublisherRetrieveUpdateDestroyView.as_view(),
        name="publishers-detail-view",
    ),
]
