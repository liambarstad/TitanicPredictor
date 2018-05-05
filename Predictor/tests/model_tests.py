from django.test import TestCase
from Predictor.models import Passenger
from Predictor.tests.factories.passenger_factory import PassengerFactory

class TestPassenger(TestCase):
    def setUp(self):
        self.passenger = PassengerFactory()

    def tearDown(self):
        self.passenger.delete()

    def test_dict(self):
        att_dict = self.passenger.to_dict()
        keys = att_dict.keys()
        self.assertIn('ticket_class', keys)
        # self.assertIn('sex', keys)
        self.assertIn('siblings_to_spouses', keys)
        self.assertIn('parents_to_children', keys)
        # self.assertIn('ticket', keys)
        self.assertIn('fare', keys)
        # self.assertIn('cabin', keys)
        # self.assertIn('embarked_from', keys)
        self.assertNotIn('passenger_type', keys)
        self.assertNotIn('passenger_name', keys)
        # self.assertNotIn('survived', keys)

    def test_url_name(self):
        url_name = self.passenger.url_name()
        self.assertEqual(url_name, 'very-dead-person')
