from django.apps import AppConfig
from django.core.management import call_command
from django.db.models.signals import post_migrate


class AgencyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "agency"

    def ready(self):
        import agency.signals

        post_migrate.connect(load_agency_data, sender=self)


def load_agency_data(sender, **kwargs):
    call_command("populate_agency_data")
