import factory

class PassengerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'Predictor.Passenger'
        django_get_or_create = (
            'passenger_type',
            'survived',
            'ticket_class',
            'passenger_name',
            'sex',
            'age',
            'siblings_to_spouses',
            'parents_to_children',
            'ticket',
            'fare',
            'cabin',
            'embarked_from',)
    passenger_type = 1
    survived = 0
    ticket_class = 2
    passenger_name = 'Person, Mr. Very Dead'
    sex = 0
    age = 52
    siblings_to_spouses = 4
    parents_to_children = 5
    ticket = 'E56'
    fare = 18233
    cabin = 'E52?'
    embarked_from = 0
