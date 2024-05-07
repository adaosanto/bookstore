from django.urls import path
from rest_framework.authtoken import views

from .views import UserCreateView, UserUpdateView

urlpatterns = [
    path("users/", UserCreateView.as_view(), name="user-create-view"),
    path("users/profile/", UserUpdateView.as_view(), name="user-update-view"),
    path("users/login/", views.obtain_auth_token),
]
