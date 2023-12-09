import os
import io
import environ
from google.cloud import secretmanager

env = environ.Env()
client = secretmanager.SecretManagerServiceClient()

if os.getenv("ENV") == "prod":
    name = "projects/{}/secrets/{}/versions/latest".format(
        os.getenv("GOOGLE_CLOUD_PROJECT"), "prod-secrets"
    )
else:
    name = "projects/{}/secrets/{}/versions/latest".format(
        os.getenv("GOOGLE_CLOUD_PROJECT"), "staging-secrets"
    )

response = client.access_secret_version(name=name).payload.data.decode("UTF-8")
env.read_env(io.StringIO(response.payload.data.decode("UTF-8")))

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
]

MIDDLEWARE = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}
