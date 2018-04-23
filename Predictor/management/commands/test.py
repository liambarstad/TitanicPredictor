from django.core.management.base import BaseCommand, CommandError
from Predictor.scripts.train import test

class Command(BaseCommand):
    help = 'tests network from test data'

    def add_arguements(self, parser):
        pass

    def handle(self, *args, **options):
        test()
