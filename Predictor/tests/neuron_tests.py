from django.test import TestCase
from py2neo import Graph, Node, Relationship
from TitanicPredictor.secrets import secrets
from Predictor.models.neuron import Neuron

class TestNeuron(TestCase):
    def setUp(self):
        self.graph = Graph(user=secrets['db_user'], password=secrets['db_pass'])

    def tearDown(self):
        self.graph.delete_all()

    def test_neuron_can_be_created(self):
        pass

    def test_neuron_can_create_relationship_with_other_neuron(self):
        pass

    def test_neuron_can_create_relationship_with_other_neurons(self):
        pass

