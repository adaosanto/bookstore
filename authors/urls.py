from django.urls import path

from .views import AuthorCreateListView, AuthorRetrieveUpdateDestroyView

urlpatterns = [
    path("authors/", AuthorCreateListView.as_view(), name="authors-create-list"),
    path(
        "authors/<int:pk>",
        AuthorRetrieveUpdateDestroyView.as_view(),
        name="authors-detail-view",
    ),
]
