from django.test import TestCase
from py2neo import Graph, Node, Relationship
from TitanicPredictor.secrets import secrets
from Predictor.models.brain import Brain
from Predictor.models.passenger import Passenger

class TestBrain(TestCase):
    def setUp(self):
        self.graph = Graph(user=secrets['db_user'], password=secrets['db_pass'])

    def tearDown(self):
        self.graph.delete_all()

    def test_brain_can_record_passenger(self):
        pass

    def test_brain_can_create_second_layer(self):
        pass

    def test_brain_can_create_third_layer(self):
        pass

    def test_brain_can_backpropogate(self):
        pass
