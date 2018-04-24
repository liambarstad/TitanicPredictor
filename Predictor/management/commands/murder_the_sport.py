from django.core.management.base import BaseCommand, CommandError
from Predictor.scripts import scrape

class Command(BaseCommand):
    help = 'kills the very nature of the competition by scraping the titanic wiki for survivor names. please hit yourself 100 times in the head with a book while humming in repentance for your sins'

    def add_arguements(self, parser):
        pass

    def handle(self, *args, **options):
        scrape()
