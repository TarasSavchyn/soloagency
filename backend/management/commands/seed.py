import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth import get_user_model

from agency.models import (
    Article,
    Service,
    Agency,
    EventType,
    Organizer,
    Event,
    Advice,
    Review,
    CallRequest,
    Portfolio,
)

User = get_user_model()
fake = Faker()

class Command(BaseCommand):
    help = "Seed database with realistic fake data"

    def handle(self, *args, **kwargs):
        # Create users
        users = []
        for _ in range(10):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password="password123"
            )
            users.append(user)

        # Articles
        articles = []
        for _ in range(5):
            articles.append(Article.objects.create(
                title=fake.sentence(nb_words=6),
                content=fake.text(max_nb_chars=500)
            ))

        # Services
        services = []
        for _ in range(5):
            services.append(Service.objects.create(
                name=fake.bs(),
                description=fake.text(max_nb_chars=511)
            ))

        # Agency (singleton)
        try:
            agency = Agency.objects.create(name=fake.company())
            agency.articles.set(articles)
            agency.services.set(services)
        except ValueError:
            agency = Agency.objects.get(id=1)

        # EventTypes
        event_types = []
        for _ in range(5):
            event_types.append(EventType.objects.create(
                name=fake.word(),
                description=fake.sentence(),
                photo="default.jpg"  # Replace with valid test image in uploads
            ))

        # Organizers
        organizers = []
        for _ in range(5):
            organizer = Organizer.objects.create(
                description=fake.paragraph(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                position=fake.job(),
                phone=fake.phone_number(),
                email=fake.email()
            )
            organizers.append(organizer)


        # Advice
        for _ in range(5):
            Advice.objects.create(
                question=fake.sentence(),
                answer=fake.text(max_nb_chars=511),
                priority=random.randint(1, 5)
            )





        self.stdout.write(self.style.SUCCESS("Realistic fake data created successfully!"))
