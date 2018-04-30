from django.test import TestCase
from Predictor.models import Passenger

class TestPassenger(TestCase):
    def setUp(self):
        Passenger.objects.create(
            passenger_type = 1,
            survived = 1,
            ticket_class = 2,
            passenger_name = 'Person, Mr. Very Dead',
            sex = 0,
            age = 52,
            siblings_to_spouses = 4,
            parents_to_children = 5,
            ticket = 'E56',
            fare = 18233,
            cabin = 'E52?',
            embarked_from = 0)
        self.passenger = Passenger.objects.get(passenger_name = 'Person, Mr. Very Dead')

    def tearDown(self):
        self.passenger.delete()

    def test_dict(self):
        att_dict = self.passenger.to_dict()
        keys = att_dict.keys()
        self.assertIn('ticket_class', keys)
        self.assertIn('sex', keys)
        self.assertIn('siblings_to_spouses', keys)
        self.assertIn('parents_to_children', keys)
        self.assertIn('ticket', keys)
        self.assertIn('fare', keys)
        self.assertIn('cabin', keys)
        self.assertIn('embarked_from', keys)
        self.assertNotIn('passenger_type', keys)
        self.assertNotIn('passenger_name', keys)
        self.assertNotIn('survived', keys)

    def test_url_name(self):
        url_name = self.passenger.url_name()
        self.assertEqual(url_name, 'very-dead-person')
