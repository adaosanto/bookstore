from django.urls import path

from .views import BookCreateListView, BookRetrieveUpdateDestroyView

urlpatterns = [
    path("books/", BookCreateListView.as_view(), name="book-create-list"),
    path(
        "books/<int:pk>",
        BookRetrieveUpdateDestroyView.as_view(),
        name="book-detail-view",
    ),
]
