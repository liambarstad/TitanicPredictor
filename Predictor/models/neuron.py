from py2neo import Node, Relationship

class Neuron:
    def __init__(self, title, **kwargs):
        self.title = title
        self.graph = kwargs.graph
        self.properties = kwargs.properties
        self.node = self.create_node(kwargs)

    def create_relationship(nodes, message, **kwargs):
        tr = self.graph.begin()
        for node in nodes:
            rel = Relationship(self.node, message, node, kwargs)
            tr.create(rel)
        tr.commit()
            

    def _create_node(self, **kwargs):
        tr = self.graph.begin()
        head = Node(self.title, self.properites.KEYWORDIMIFIZE) 
        tr.create(head)
        if tr.commit():
            return head

