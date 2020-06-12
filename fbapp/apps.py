from django.apps import AppConfig


class FbappConfig(AppConfig):
    name = 'fbapp'

    def ready(self):
        import fbapp.signals