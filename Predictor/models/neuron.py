from py2neo.ogm import GraphObject, Property

'''
class Neuron:
    def __init__(self, title, graph, **kwargs):
        self.title = title
        self.graph = graph
        self.properties = kwargs
        self.node = self._create_node()

    def create_relationship(nodes, message, **kwargs):
        tr = self.graph.begin()
        for node in nodes:
            rel = Relationship(self.node, message, node, kwargs)
            tr.create(rel)
        tr.commit()
            

    def _create_node(self):
        tr = self.graph.begin()
        head = Node(self.title, self.properites.KEYWORDIMIFIZE) 
        tr.create(head)
        tr.commit()
        return head
'''
