from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Import live games from API'

    def handle(self, *args, **kwargs):
        pass