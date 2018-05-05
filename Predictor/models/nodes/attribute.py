from Predictor.models.nodes.application_graph_object import ApplicationGraphObject
from py2neo.ogm import Property

class Attribute(ApplicationGraphObject):
    __primarykey__ = 'attribute_name'
    
    attribute_name = Property('attribute_name')
    value = Property('value') 
    weight = Property('weight')
    bias = Property('bias')
