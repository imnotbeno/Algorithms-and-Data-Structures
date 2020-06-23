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

    def add_edge(self, source, destination):
        node = Node(destination)
        node.next = self.graph[source]
        self.graph[source] = node

        node = Node(source)
        node.next = self.graph[destination]
        self.graph[destination] = node

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n ".format(i), end=" ")
            tmp = self.graph[i]
            print(" -> {}".format(tmp.vertex), end=" ")
            tmp = tmp.next
        
if __name__ == "__main__":

    graph = Graph(5)
    graph.add_edge(0,1)
    graph.add_edge(1,2)
    graph.add_edge(2,3)
    graph.add_edge(3,4)

    graph.print_graph()