from django.apps import AppConfig
from django.core.management import call_command
from django.db.models.signals import post_migrate


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user"

    def ready(self):
        import agency.signals

        post_migrate.connect(load_user_data, sender=self)


def load_user_data(sender, **kwargs):
    call_command("populate_user_data")
