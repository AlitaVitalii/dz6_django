from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):
    help = 'Create user'

    def add_arguments(self, parser):
        parser.add_argument('numb', type=int, choices=range(1, 11))

    def handle(self, *args, **options):
        fake = Faker()
        p = User.objects.bulk_create([User(
            username=fake.name(),
            email=fake.email(),
            password=make_password(fake.password())
        ) for _ in range(options['numb'])])

        self.stdout.write(self.style.SUCCESS(f"Cозданы пользователи: {p}"))
