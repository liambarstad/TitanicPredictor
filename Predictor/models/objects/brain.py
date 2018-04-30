from py2neo import Graph
from py2neo.ogm import RelatedObjects
from Predictor.models.nodes import *
from TitanicPredictor.secrets import secrets

class Brain:
    def __init__(self):
        self.graph = Graph(user=secrets['db_user'], password=secrets['db_pass'])

    def add_passenger(self, passenger):
        new_passenger = Person()
        new_passenger.name = passenger.passenger_name
        for key, value in passenger.to_dict():
            attribute = Attribute()
            attribute.attribute_name = key
            attribute.value = value
            new_passenger.attributes.add(attribute) 
        self.graph.push(new_passenger)
        # add Passenger node 'Passenger'
        # initialize into numpy array
        # train
        # train_secondary
        # train_tertiary
        # answer
        # if passenger is training, backpropogate

