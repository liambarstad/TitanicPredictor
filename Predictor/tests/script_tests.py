from django.test import TestCase
from Predictor.scripts.train import train

class TestScripts(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        Passenger.objects.clear()
        self.graph.delete_all()

    def test_train(self):
        passengers = PassengerFactory.create_batch(10, passenger_type=0)
        train()
        attrs = list(Attribute.select(self.graph))
        self.assertEqual(len(attrs), 5)
