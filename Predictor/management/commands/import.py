import csv
#import django
from django.core.management.base import BaseCommand, CommandError
from Predictor.models import Passenger

class Command(BaseCommand):
    help = 'imports and seeds data from csv'

    def add_arguements(self, parser):
        pass

    def handle(self, *args, **options):
        with open("./Predictor/data/train.csv") as f:
            reader = csv.reader(f)
            try:
                next(reader, None)
                for row in reader:
                    _ = Passenger.objects.csv_create(row)
            except csv.Error as error:
                sys.exit(error)
