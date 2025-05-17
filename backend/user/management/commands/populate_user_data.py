from django.core.management.base import BaseCommand
from user.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.populate_superuser()

    def populate_superuser(self, *args, **kwargs):
        if not User.objects.filter(email="soloagency2000@gmail.com").exists():
            User.objects.create_user(
                email="soloagency2000@gmail.com",
                password="taras-123",
                is_staff=True,
                first_name="Admin",
                last_name="User",
            )
            self.stdout.write(self.style.SUCCESS("Created test user"))
        else:
            self.stdout.write("User вже існує — пропущено")
