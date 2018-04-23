from django.db import models

class PassengerManager(models.Manager):
    def csv_create(self, row):
        print(row)

class Passenger(models.Model):
    survived = models.IntegerField()
    # 0 => ded
    ticket_class = models.IntegerField()
    # 1-3
    passenger_name = models.CharField(max_length=20)
    sex = models.IntegerField()
    # ^ comes in as male/female
    age = models.IntegerField()
    # in years
    siblings_to_spouses = models.IntegerField()
    parents_to_children = models.IntegerField()
    ticket_number = models.IntegerField()
    fare = models.IntegerField()
    # ^ comes in as string/float
    cabin_number = models.CharField(max_length=4, null=True)
    embarked_from = models.IntegerField()
    # ^ C = Cherbourg, Q = Queenstown, S = Southampton

    objects = PassengerManager()
