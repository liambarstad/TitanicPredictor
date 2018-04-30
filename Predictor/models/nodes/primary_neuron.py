from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedFrom

class PrimaryNeuron(GraphObject):
    activation = Property('activation')

    attributes = RelatedFrom('Attribute', 'FROM_ATTRIBUTE')
    next_layer = RelatedTo('SecondaryNeuron', 'LEADS_TO')
