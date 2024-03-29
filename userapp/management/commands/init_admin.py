import os
from django.core.management.base import BaseCommand

from userapp.models import User


class Command(BaseCommand):
    help = 'Command to create a superuser if none exists'

    def handle(self, *args, **kwargs):
        if os.environ.get('CREATE_DJANGO_SUPERUSER') == 'yes':
            if not User.objects.filter(username='test@admin.com').exists():
                User.objects.create_superuser(
                    'test@admin.com', 'test@admin.com', 'mysecretpassword')
                self.stdout.write(self.style.SUCCESS(
                    'Superuser created successfully'))
            else:
                self.stdout.write(self.style.WARNING(
                    'Superuser already exists'))
