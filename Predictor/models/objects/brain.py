from py2neo import Graph
from py2neo.ogm import RelatedObjects
from Predictor.models.nodes.person import Person
from Predictor.models.nodes.attribute import Attribute
from TitanicPredictor.secrets import secrets

class Brain:
    def __init__(self):
        self.graph = Graph(user=secrets['db_user'], password=secrets['db_pass'])

    def calculate_passenger(self, passenger):
        pass 
        # add all steps together

    def add_passenger(self, passenger):
        new_passenger = Person()
        new_passenger.name = passenger.passenger_name
        for key, value in passenger.to_dict().items():
            attribute = Attribute()
            attribute.attribute_name = key
            attribute.value = value
            new_passenger.create_relationship(self.graph, attribute, 'HAS_ATTRIBUTE')
        self.graph.push(new_passenger)

    def create_primary_layer(subgraph):
        pass
        # values => numpy array
        # sig(np_arr)
        # all possible permutations
        # if Pn DNE, add wa + b, or (1)a + 0
        # if Pn !E, put a through function, edit corresponding node
    
    def create_secondary_layer(subgraph):
        pass
