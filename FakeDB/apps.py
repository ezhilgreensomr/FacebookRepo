from django.apps import AppConfig


class FakedbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FakeDB'
