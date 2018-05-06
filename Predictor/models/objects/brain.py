import pdb
from math import exp
from py2neo import Graph
from py2neo.ogm import RelatedObjects
from Predictor.models.nodes.person import Person
from Predictor.models.nodes.attribute import Attribute
from Predictor.models.nodes.primary_neuron import PrimaryNeuron
from TitanicPredictor.secrets import secrets

class Brain:
    attr_ledger = [
        'ticket_class',
        # 'sex',
        'siblings_to_spouses',
        'parents_to_children',
        # 'ticket',
        'age',
        'fare',
        # 'cabin',
        # 'embarked_from',
            ]

    def __init__(self):
        self.graph = Graph(user=secrets['db_user'], password=secrets['db_pass'])
        self._initialize_attrs()
        self.queued_changes = {}

    def calculate_passenger(self, passenger):
        '''
        self.add_passenger(passenger)
        primary_neuron = self.add_primary_neuron()
        result = self.calculate_result(primary_neuron)
        return result
        '''

    def add_passenger(self, passenger):
        new_passenger = Person()
        new_passenger.name = passenger.passenger_name
        passenger_attrs = passenger.to_dict()
        survived = passenger_attrs.pop('survived')
        new_passenger.result = survived
        self._add_passenger_values(new_passenger, passenger_attrs)
        return new_passenger

    def add_primary_neuron(self):
        primary_neuron = PrimaryNeuron()
        primary_neuron.activation = 0
        for attribute in Attribute.select(self.graph):
            attribute.create_relationship(self.graph, primary_neuron, 'HAS_NEURON')
            primary_neuron.activation += (attribute.weight * attribute.value) + attribute.bias
        primary_neuron.activation = self._sigmoid(primary_neuron.activation)
        self.graph.push(primary_neuron)
        return primary_neuron

    def calculate_result(self, primary_neuron):
        if primary_neuron.results
            self.backpropogate(primary_neuron)
        else:
            return primary_neuron.results
        # if primary_neuron has result, backpropogate
        # else, calculate

    def backpropogate(self, primary_neuron):
        for attr in Attribute.select(self.graph):
            raw_value = (attr.weight * attr.value) + attr.bias
            sig_deriv = scipy.misc.derivative(self._sigmoid, raw_value, order=7)
            bias_nudge = sig_deriv * 2 * (primary_neuron.activation - primary_neuron.results)
            weight_nudge = attr.value * bias_nudge

        # add up squares of differences as cost 
        # find closest local minimum of cost function (r)
        pass

    def _add_passenger_values(self, person_obj, attr_dict):
        for key, value in attr_dict.items():
            attribute = Attribute.select(self.graph).where(f"_.attribute_name = '{key}'").first()
            attribute.value = value
            self.graph.push(attribute)
            person_obj.create_relationship(self.graph, attribute, 'HAS_ATTRIBUTE')
        self.graph.push(person_obj)

    def _initialize_attrs(self):
        for attr in self.attr_ledger:
            attribute = Attribute()
            attribute.attribute_name = attr
            attribute.weight = 1
            attribute.bias = 0
            self.graph.push(attribute)

    def _sigmoid(self, num):
        return float(1 / (1 + exp(-num)))
