from py2neo.ogm import GraphObject, Property, RelatedTo

class Person(GraphObject):
    __primarykey__ = 'name'

    name = Property('name')

    attributes = RelatedTo('Attribute', 'HAS_ATTRIBUTE')
