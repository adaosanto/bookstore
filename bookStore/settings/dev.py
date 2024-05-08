from .base import *

SECRET_KEY = "dev"
DEBUG = True
ALLOWED_HOSTS = ["*"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
CSRF_TRUSTED_ORIGINS = ["http://localhost:8000"]
