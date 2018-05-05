from Predictor.models.nodes.application_graph_object import ApplicationGraphObject
from py2neo.ogm import Property

class Person(ApplicationGraphObject):
    __primarykey__ = 'name'

    name = Property('name')
    result = Property('result')
