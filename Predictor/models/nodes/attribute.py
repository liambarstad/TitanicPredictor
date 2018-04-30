from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedFrom

class Attribute(GraphObject):
    __primarykey__ = 'attribute_name'
    
    attribute_name = Property('attribute_name')
    value = Property('value') 

    passenger = RelatedFrom('Passenger', 'HAS_ATTRIBUTE') 
    neurons = RelatedTo('PrimaryNeuron', 'LEADS_TO')
    # ^ add relational properties
