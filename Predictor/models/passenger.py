from Predictor.models.passenger_manager import PassengerManager
from django.db import models

class Passenger(models.Model):
    passenger_type = models.IntegerField()
    survived = models.IntegerField()
    ticket_class = models.IntegerField()
    passenger_name = models.CharField(max_length=20)
    sex = models.IntegerField()
    age = models.IntegerField()
    siblings_to_spouses = models.IntegerField()
    parents_to_children = models.IntegerField()
    ticket = models.CharField(default='none', max_length=12)
    fare = models.IntegerField()
    cabin = models.CharField(max_length=10, default='unknown')
    embarked_from = models.IntegerField()

    objects = PassengerManager()

    def url_name(self):
        name_arr = self.passenger_name.split()
        name_arr.pop('Mr.', 'Mrs.')
        if name_arr[0]:
            last_name = name_arr.unshift()
            name_arr.shift(last_name)
        name_arr.map('...')
        # ^ make lowercase
        return name_arr.join('-')
