from Predictor.models.nodes.application_graph_object import ApplicationGraphObject
from py2neo.ogm import Property

class PrimaryNeuron(ApplicationGraphObject):
    activation = Property('activation')
    result = Property('result')
