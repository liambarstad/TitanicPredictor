'''
from django.test import TestCase
from py2neo import Graph, Node, Relationship, NodeSelection
from TitanicPredictor.secrets import secrets
from Predictor.models.neuron import Neuron

class TestNeuron(TestCase):
    def setUp(self):
        self.graph = Graph(user=secrets['db_user'], password=secrets['db_pass'])

    def tearDown(self):
        self.graph.delete_all()

    def test_neuron_can_be_created(self):
        neuron = Neuron('thing', graph=self.graph, prop1='this', prop2='that')
        db_neuron = NodeSelection(self.graph).first()

        self.assertEqual(neuron.title, 'thing')
        self.assertEqual(neuron.properties, { 'prop1':'this', 'prop2':'that' })
        self.assertTrue(db_neuron.has_label('thing'))

    def test_neuron_can_create_relationship_with_other_neuron(self):
        pass

    def test_neuron_can_create_relationship_with_other_neurons(self):
        pass
'''
