from django.db import models

class PassengerManager(models.Manager):
    def csv_create(self, row, purpose):
        return self.get_or_create(
            passenger_type=self.format_passenger_type(purpose), 
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

    def format_passenger_type(purpose):
        purposes = {'train': 0, 'test': 1, 'consumer': 2}
        return purposes[purpose]

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

