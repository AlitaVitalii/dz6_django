from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Delete_users'

    def add_arguments(self, parser):
        parser.add_argument('arg1', nargs='+', type=int)

    def handle(self, *args, **options):
        my_list = options['arg1']
        for i in my_list:
            u1 = User.objects.get(is_superuser=1)
            u2 = User.objects.get(pk=i)
            if u1 == u2:
                self.stdout.write(self.style.SUCCESS(f"Удалите суперпользователя c id-{u1.id} из списка"))
                exit()
        for i in my_list:
            User.objects.get(pk=i).delete()

        self.stdout.write(self.style.SUCCESS(f"Удалены пользователи с id: {my_list}"))
