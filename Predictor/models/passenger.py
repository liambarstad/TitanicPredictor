import re
from Predictor.models.passenger_manager import PassengerManager
from django.db import models
from django.forms.models import model_to_dict

class Passenger(models.Model):
    passenger_type = models.IntegerField()
    # metadata
    survived = models.IntegerField()
    # result
    ticket_class = models.IntegerField()
    passenger_name = models.CharField(max_length=20)
    sex = models.IntegerField()
    # binning -> relative average
    age = models.IntegerField()
    siblings_to_spouses = models.IntegerField()
    parents_to_children = models.IntegerField()
    ticket = models.CharField(default='none', max_length=12)
    # quantify ticket
    fare = models.IntegerField()
    cabin = models.CharField(max_length=10, default='unknown')
    # quantify cabin
    embarked_from = models.IntegerField()
    # binning -> relative average

    objects = PassengerManager()

    def to_dict(self):
        attrs = model_to_dict(self)
        attrs.pop('passenger_name')
        attrs.pop('passenger_type')
        attrs.pop('id')
        # metadata
        attrs.pop('sex')
        attrs.pop('ticket')
        # binning
        attrs.pop('cabin')
        attrs.pop('embarked_from')
        # need to quantify

        # attrs.pop('survived')
        return attrs

    def url_name(self):
        name_arr = self.passenger_name.split()
        if 'Mr.' in name_arr: name_arr.remove('Mr.')
        if 'Mrs.' in name_arr: name_arr.remove('Mrs.')
        last_name = name_arr.pop(0)
        name_arr.append(last_name)
        name = '-'.join(name_arr).lower()
        return re.sub('[,. ]', '', name)
