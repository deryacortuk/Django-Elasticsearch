from django.apps import AppConfig


class ColinfoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "colinfo"
    def ready(self):
        import colinfo.signals
