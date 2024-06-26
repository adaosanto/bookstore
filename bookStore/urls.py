"""
URL configuration for bookStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="BookStore API",
        default_version="v1",
        description="Manager your books",
        contact=openapi.Contact(email="adaosantosn@outlook.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

admin.site.site_title = "BookStore Admin"
admin.site.site_header = "BookStore Admin"
admin.site.index_title = "BookStore Admin"
admin.site.site_url = '/swagger'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("books.urls")),
    path("api/v1/", include("authors.urls")),
    path("api/v1/", include("genres.urls")),
    path("api/v1/", include("languages.urls")),
    path("api/v1/", include("publishers.urls")),
    path("api/v1/", include("users.urls")),
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
