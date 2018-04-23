from django.db import models

class PassengerManager(models.Manager):
    def csv_create(self, row):
        return self.get_or_create(
            survived=self.format_int(row[1]),
            ticket_class=self.format_int(row[2]),
            passenger_name=row[3],
            sex=self.format_sex(row[4]),
            age=self.format_int(row[5]),
            siblings_to_spouses=self.format_float(row[6]),
            parents_to_children=self.format_float(row[7]),
            ticket=row[8],
            fare=self.format_float(row[9]),
            cabin=row[10],
            embarked_from=self.format_embarked_from(row[11]),
                )[0]

    def format_int(self, value):
        if value:
            return int(float(value))
        else:
            return 0

    def format_float(self, value):
        if value:
            return int(10000 * float(value))
        else:
            return 42

    def format_sex(self, sex):
        if sex:
            sexes = {'male': 0, 'female': 1}
            return sexes[sex]
        else:
            return 2

    def format_embarked_from(self, letter):
        if letter:
            stops = {'C': 0, 'Q': 1, 'S': 2}
            # ^ C = Cherbourg, Q = Queenstown, S = Southampton
            return stops[letter]
        else: 
            return 3

class Passenger(models.Model):
    survived = models.IntegerField()
    ticket_class = models.IntegerField()
    passenger_name = models.CharField(max_length=20)
    sex = models.IntegerField()
    # unknown set to 2
    age = models.IntegerField()
    # unknown set to 0
    siblings_to_spouses = models.IntegerField()
    # default set to 42
    parents_to_children = models.IntegerField()
    # default set to 42
    ticket = models.CharField(default='none', max_length=12)
    fare = models.IntegerField()
    cabin = models.CharField(max_length=10, default='unknown')
    # default set to unknown
    embarked_from = models.IntegerField()
    # default set to 3

    objects = PassengerManager()
