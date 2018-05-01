from django.test import TestCase
from py2neo import Graph, Node, Relationship
from TitanicPredictor.secrets import secrets
from Predictor.models.objects.brain import Brain
from Predictor.models.nodes.person import Person
from Predictor.models.nodes.attribute import Attribute
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
        self.assertEqual(len(new_attrs), 10)
        self.assertEqual(new_person.name, passenger.passenger_name) 

    def test_brain_can_create_second_layer(self):
        pass

    def test_brain_can_create_third_layer(self):
        pass

    def test_brain_can_backpropogate(self):
        pass
