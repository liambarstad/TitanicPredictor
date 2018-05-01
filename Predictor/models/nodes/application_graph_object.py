from py2neo import Relationship
from py2neo.ogm import GraphObject

class ApplicationGraphObject(GraphObject):

    def create_relationship(self, graph, node, name, **kwargs):
        this_node = self.__ogm__.node 
        that_node = node.__ogm__.node
        rel = Relationship(this_node, name, that_node, **kwargs)
        graph.create(rel)
