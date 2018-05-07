import pdb
from math import exp
from py2neo import Graph
from py2neo.ogm import RelatedObjects
from scipy.misc import derivative
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
        self.initialize_attrs()
        self.queued_changes = {}

    def initialize_attrs(self):
        for attr in self.attr_ledger:
            attribute = Attribute()
            attribute.attribute_name = attr
            attribute.weight = 1
            attribute.bias = 0
            self.graph.push(attribute)

    def calculate_passenger(self, passenger):
        self._add_passenger(passenger)
        primary_neuron = self._add_primary_neuron(passenger.survived)
        result = self._calculate_result(primary_neuron)
        return result

    def push_queue(self):
        for name, info in self.queued_changes.items():
            attribute = Attribute.select(self.graph).where(f"_.attribute_name = '{name}'").first()
            weight = info['weight'] / info['total']
            bias = info['bias'] / info['total']
            attribute.weight += weight
            attribute.bias += bias
            self.graph.push(attribute)

    def _add_passenger(self, passenger):
        new_passenger = Person()
        new_passenger.name = passenger.passenger_name
        passenger_attrs = passenger.to_dict()
        survived = passenger_attrs.pop('survived')
        new_passenger.result = survived
        self._add_passenger_values(new_passenger, passenger_attrs)
        return new_passenger

    def _add_primary_neuron(self, result=None):
        primary_neuron = PrimaryNeuron()
        primary_neuron.activation = 0
        for attribute in Attribute.select(self.graph):
            attribute.create_relationship(self.graph, primary_neuron, 'HAS_NEURON')
            primary_neuron.activation += (attribute.weight * attribute.value) + attribute.bias
        primary_neuron.activation = self._sigmoid(primary_neuron.activation)
        primary_neuron.result = result
        self.graph.push(primary_neuron)
        return primary_neuron

    def _calculate_result(self, primary_neuron):
        if isinstance(primary_neuron.result, (int, float)):
            self._backpropogate(primary_neuron)
            return None
        else:
            return primary_neuron.result

    def _backpropogate(self, primary_neuron):
        for attr in Attribute.select(self.graph):
            raw_value = (attr.weight * attr.value) + attr.bias
            sig_deriv = derivative(self._sigmoid, raw_value, order=7)
            bias_nudge = sig_deriv * 2 * (primary_neuron.activation - primary_neuron.result)
            weight_nudge = attr.value * bias_nudge
            self._add_to_queue(attr.attribute_name, weight_nudge, bias_nudge)


    def _add_passenger_values(self, person_obj, attr_dict):
        for key, value in attr_dict.items():
            attribute = Attribute.select(self.graph).where(f"_.attribute_name = '{key}'").first()
            attribute.value = value
            self.graph.push(attribute)
            person_obj.create_relationship(self.graph, attribute, 'HAS_ATTRIBUTE')
        self.graph.push(person_obj)

    def prune(self):
        Person.select(self.graph).delete()
        PrimaryNeuron.select(self.graph).delete()

    def clear(self):
        self.graph.delete_all()

    def _sigmoid(self, num):
        return float(1 / (1 + exp(-num)))

    def _add_to_queue(self, attr_name, weight, bias):
        if attr_name in self.queued_changes:
            self.queued_changes[attr_name]['weight'] += weight
            self.queued_changes[attr_name]['bias'] += bias
            self.queued_changes[attr_name]['total'] += 1.0
        else:
            self.queued_changes[attr_name] = {
                    'weight': weight,
                    'bias': bias,
                    'total': 1.0,
                    }
