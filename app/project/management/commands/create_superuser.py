from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from project.settings import SUPERUSER_USERNAME, SUPERUSER_EMAIL, SUPERUSER_PASSWORD


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--username')
        parser.add_argument('--email')
        parser.add_argument('--password')
        parser.add_argument('--no-input', action='store_true')

    def handle(self, *args, **options):
        User = get_user_model()

        if SUPERUSER_USERNAME and SUPERUSER_EMAIL and SUPERUSER_PASSWORD:
            if options['no_input']:
                options['username'] = SUPERUSER_USERNAME
                options['email'] = SUPERUSER_EMAIL
                options['password'] = SUPERUSER_PASSWORD

            if not User.objects.filter(username=options['username']).exists():
                User.objects.create_superuser(
                    username=options['username'],
                    email=options['email'],
                    password=options['password'],
                )
