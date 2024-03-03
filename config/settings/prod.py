import environ

from .base import *

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(str(BASE_DIR / ".env.prod"))

THIRD_PARTY_APP = [
    "django_extensions",
]  # third party apps goe here

INSTALLED_APPS = INSTALLED_APPS + THIRD_PARTY_APP

SECRET_KEY = env.str("SECRET_KEY")
DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]  # modify later
CSRF_TRUSTED_ORIGINS = []  # modify later


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": env.str("DB_NAME"),
#         "USER": env.str("DB_USER"),
#         "PASSWORD": env.str("DB_PWD"),
#         "HOST": env.str("DB_HOST"),
#         "PORT": env.str("DB_PORT"),
#     }
# }

# If you want to use sqlite3 instead, then uncomment this and comment the above.

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

STATIC_ROOT = str(BASE_DIR.joinpath("staticfiles"))
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (str(BASE_DIR.joinpath("static")),)

import dj_database_url

DATABASE_URL = env.str("DATABASE_URL")

DATABASES = {
    "default": dj_database_url.config(default=DATABASE_URL)  # , conn_max_age=1800),
}
