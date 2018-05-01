from django.test import TestCase
from py2neo import Graph, Node, Relationship
from TitanicPredictor.secrets import secrets
from Predictor.models.objects.brain import Brain
from Predictor.models import Passenger
from Predictor.tests.factories.passenger_factory import PassengerFactory

class TestBrain(TestCase):
    def setUp(self):
        self.graph = Graph(user=secrets['db_user'], password=secrets['db_pass'])
        self.brain = Brain()

    def tearDown(self):
        self.graph.delete_all()

    def test_brain_can_record_passenger(self):
        passenger = PassengerFactory
        self.brain.add_passenger(passenger)
        # expect passenger node
        # expect each attribute node

    def test_brain_can_create_second_layer(self):
        pass

    def test_brain_can_create_third_layer(self):
        pass

    def test_brain_can_backpropogate(self):
        pass
