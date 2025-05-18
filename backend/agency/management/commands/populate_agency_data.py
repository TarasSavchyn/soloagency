from django.core.management.base import BaseCommand
from agency.models import Service, Agency, Article, EventType, Organizer, Advice
from django.core.files.base import ContentFile
from io import BytesIO
from PIL import Image


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.populate_services()
        self.populate_articles_and_agency()
        self.populate_event_types()
        self.populate_organizers()
        self.populate_advice()

    def populate_services(self):
        if not Service.objects.exists():
            Service.objects.create(
                name="Організація весіль",
                description="Повний супровід події: від сценарію до реалізації.",
            )
            Service.objects.create(
                name="Корпоративи", description="Свята для компаній під ключ."
            )
            self.stdout.write(self.style.SUCCESS("Services створено"))
        else:
            self.stdout.write("Services вже існують — пропущено")

    def populate_articles_and_agency(self):
        if not Agency.objects.exists():
            a1 = Article.objects.create(
                title="Наш підхід", content="Ми працюємо якісно."
            )
            a2 = Article.objects.create(
                title="Історія агенції", content="Почали з мрії."
            )

            s1 = Service.objects.first()
            agency = Agency(name="EventPro")
            agency.save()
            agency.articles.set([a1, a2])
            agency.services.set([s1])
            self.stdout.write(self.style.SUCCESS("Agency і статті створено"))
        else:
            self.stdout.write("Agency вже існує — пропущено")

    def create_dummy_image(self, name="test.jpg"):
        image = Image.new("RGB", (100, 100), color="white")
        byte_io = BytesIO()
        image.save(byte_io, "JPEG")
        return ContentFile(byte_io.getvalue(), name)

    def populate_event_types(self):
        if not EventType.objects.exists():
            photo = self.create_dummy_image("event_type.jpg")
            EventType.objects.create(
                name="Весілля",
                description="Романтична подія для двох і гостей",
                photo=photo,
            )
            self.stdout.write(self.style.SUCCESS("EventTypes створено"))
        else:
            self.stdout.write("EventTypes вже існують — пропущено")

    def populate_organizers(self):
        if not Organizer.objects.exists():
            Organizer.objects.create(
                first_name="Олена",
                last_name="Петренко",
                position="Координатор",
                description="Досвідчений організатор з 5-річним досвідом",
                phone="+380991112233",
                email="olena@example.com",
            )
            self.stdout.write(self.style.SUCCESS("Organizer створено"))
        else:
            self.stdout.write("Organizer вже існує — пропущено")

    def populate_advice(self):
        if not Advice.objects.exists():
            Advice.objects.create(
                question="Як вибрати локацію?",
                answer="Обирайте місце відповідно до стилю та кількості гостей.",
                priority=3,
            )
            self.stdout.write(self.style.SUCCESS("Advice створено"))
        else:
            self.stdout.write("Advice вже існує — пропущено")
