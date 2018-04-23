from models import Passenger
from py2neo import Graph

class Brain:
    def __init__(self):
        self.graph = Graph()

    def add_passenger(self, passenger):
        # all aboard the brain train
        transaction = self.graph.begin()
        head = Node('Passenger', name=passenger.passenger_name)
        transaction.create(head)
        attributes = passenger.values()
        for name, value in attributes:
            new_node = Node('Attribute', name=name, value=value)
            tether = Relationship(head, 'has attribute', new_node)
            transaction.create(tether) 
        transaction.commit()
        # add Passenger node 'Passenger'
        # initialize into numpy array
        # train
        # train_secondary
        # train_tertiary
        # answer
        # if passenger is training, backpropogate

    def _train(self, passenger):
        # choo choo

        # find activation groups
        # if activation groups exist, plug into numpy array
        # second_selection

    def _train_secondary(self, bleh):
        # same shit

    def _train_tertiary(self, bleh):
        # more of the same shit

    def _answer(self, bleh):
        # fuck it

    def _backpropogate(self, bleh):
        # shit son

# input Passenger object

# create passenger - Subgraph(Nodes, relationships)
# 1 Passenger node w/ survived
# 10 Nodes for each Passenger Subgraph
# each node labeled by quality

# create next node collection
    # create nodes by activation groups(sigmoid for large integers)

# create next node collection by activation


