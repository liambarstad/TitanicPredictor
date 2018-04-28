import csv
from django.core.management.base import BaseCommand, CommandError
from Predictor.models.passenger import Passenger

class Command(BaseCommand):
    help = 'imports and seeds data from csv'

    def add_arguements(self, parser):
        pass

    def handle(self, *args, **options):
        with open("./Predictor/data/train.csv") as f:
            reader = csv.reader(f)
            ind = 0
            try:
                next(reader, None)
                for row in reader:
                    ind += 1
                    passenger = Passenger.objects.csv_create(row, 'train')
                    print("passenger {passenger_name} created".format(passenger_name=passenger.passenger_name))
            except csv.Error as error:
                sys.exit("{error} at line ${ind}".format(error, ind))
