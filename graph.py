# !python3

# class to create a vertex/node
class Node:

    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None 

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    #def add_edge(self, source, destination):

