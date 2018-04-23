from django.core.management.base import BaseCommand, CommandError
from Predictor.scripts.train import train

class Command(BaseCommand):
    help = 'trains network from training data'

    def add_arguements(self, parser):
        pass

    def handle(self, *args, **options):
        train()
