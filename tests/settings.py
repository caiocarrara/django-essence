SECRET_KEY = "django-essence-test-secret-key"

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django_essence",
    "tests",
]

DATABASES = {
    "default": {"NAME": "db.sqlite", "ENGINE": "django.db.backends.sqlite3",},
}
