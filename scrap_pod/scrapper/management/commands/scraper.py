from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Scrap the data then dump in Products Table'

    def handle(self, *args, **kwargs):
        
        pass