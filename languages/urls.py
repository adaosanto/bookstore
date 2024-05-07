from django.urls import path

from .views import LanguageCreateListView, LanguageRetrieveUpdateDestroyView

urlpatterns = [
    path("languages/", LanguageCreateListView.as_view(), name="languages-create-list"),
    path(
        "languages/<int:pk>",
        LanguageRetrieveUpdateDestroyView.as_view(),
        name="languages-detail-view",
    ),
]
