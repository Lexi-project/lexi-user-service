import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Command to create a superuser if none exists'

    def handle(self, *args, **kwargs):
        if os.environ.get('CREATE_DJANGO_SUPERUSER') == 'yes':
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser(
                    'admin', 'first@admin.com', 'mysecretpassword')
                self.stdout.write(self.style.SUCCESS(
                    'Superuser created successfully'))
            else:
                self.stdout.write(self.style.WARNING(
                    'Superuser already exists'))
