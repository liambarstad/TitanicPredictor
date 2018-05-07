import csv
from django.core.management.base import BaseCommand, CommandError
from Predictor.models.passenger import Passenger

class Command(BaseCommand):
    help = 'imports and seeds data from csv'

    def add_arguments(self, parser):
        parser.add_argument(
                '--train',
                action='store_true',
                dest='train',
                help='import training data',
                )
        parser.add_argument(
                '--check',
                action='store_true',
                dest='check',
                help='import check(test) data',
                )

    def handle(self, *args, **options):
        if options['train']:
            self.import_train()
        elif options['check']:
            self.import_check()
        else:
            self.import_train()
            self.import_check()

    def import_train(self):
        Passenger.objects.filter(passenger_type=0).delete()
        with open('./Predictor/data/train.csv') as f:
            reader = csv.reader(f)
            ind = 0
            try:
                next(reader, None)
                for row in reader:
                    ind += 1
                    passenger = Passenger.objects.csv_create(row, 'train')
                    print(f"passenger {passenger.passenger_name} created")
            except csv.Error as error:
                raise CommandError(f"{error} at line {ind}")

    def import_check(self):
        Passenger.objects.filter(passenger_type=1).delete()
        with open('./Predictor/data/test.csv') as f:
            reader = csv.reader(f)
            ind = 0
            try: 
                next(reader, None)
                for row in reader:
                    ind += 1
                    passenger = Passenger.objects.csv_create(row, 'check')
                    print(f"passenger{passenger.passenger_name} created")
            except csv.Error as error:
                raise CommandError(f"{error} at line {ind}")
