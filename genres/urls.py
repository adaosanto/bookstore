from django.urls import path

from .views import GenreCreateListView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    path("genres/", GenreCreateListView.as_view(), name="genres-create-list"),
    path(
        "genres/<int:pk>",
        GenreRetrieveUpdateDestroyView.as_view(),
        name="genres-detail-view",
    ),
]
