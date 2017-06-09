from django.apps import AppConfig


class MyAppConfig(AppConfig):
    name = 'gettingstarted'

    def ready(self):
        # Makes sure all signal handlers are connected
        from . import handlers  # noqa