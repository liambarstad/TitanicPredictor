from django.test import TestCase
from py2neo import Graph, Node, Relationship
from TitanicPredictor.secrets import secrets
from Predictor.models.objects.brain import Brain
from Predictor.models.nodes.person import Person
from Predictor.models.nodes.attribute import Attribute
from Predictor.models.nodes.primary_neuron import PrimaryNeuron
from Predictor.models import Passenger
from Predictor.tests.factories.passenger_factory import PassengerFactory

class TestBrain(TestCase):
    def setUp(self):
        self.graph = Graph(user=secrets['db_user'], password=secrets['db_pass'])
        self.brain = Brain()

    def tearDown(self):
        self.graph.delete_all()

    def test_brain_can_record_passenger(self):
        passenger = PassengerFactory()
        self.brain.add_passenger(passenger)
        new_people = list(Person.select(self.graph)) 
        new_attrs = list(Attribute.select(self.graph))
        new_person = Person.select(self.graph).first()

        self.assertEqual(len(new_people), 1)
        self.assertEqual(len(new_attrs), 5)
        self.assertEqual(new_person.name, passenger.passenger_name) 
        self.assertEqual(new_attrs[0].weight, 1)
        self.assertEqual(new_attrs[0].bias, 0)

    def test_brain_can_record_passengers_with_missing_data(self):
        pass

    def test_brain_can_create_single_primary_neuron(self):
        passenger = PassengerFactory()
        person = self.brain.add_passenger(passenger)
        self.brain.add_primary_neuron()
        new_neuron = PrimaryNeuron.select(self.graph).first()
        self.assertEqual(new_neuron.activation, 1)

    def test_brain_can_backpropogate_single_neuron(self):
        pass
        '''
        passenger = PassengerFactory()
        self.brain.add_passenger(passenger)
        old_attrs = list(Attribute.select(self.graph))
        old_weight = old_attrs[0].weight
        old_bias = old_attrs[0].bias

        self.brain.calculate_passenger(passenger)
        new_attrs = list(Attribute.select(self.graph))
        new_weight = new_attrs[0].weight
        new_bias = new_attrs[0].bias

        self.assertNotEqual(old_weight, new_weight)
        self.assertNotEqual(old_bias, new_bias)
        '''

    def test_brain_can_add_next_neuron(self):
        pass

    def test_brain_can_backpropogate_next_neuron(self):
        pass
