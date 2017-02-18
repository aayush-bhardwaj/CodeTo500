'''
TBA : Deletion of vertex and edge
'''

import sys

class Vertex:
    def __init__(self,node):
        self.id = node
        self.adjacent= {}

    def addNeighbour(self, to , cost=0):
        self.adjacent[to] = cost

    def getConnections(self):
        return self.adjacent.keys()

    def getVertex(self):
        return self.id

    def getWeight(self, neighbour):
        return self.adjacent[neighbour]

class Graph:
    def __init__(self):
        self.num_vertices = 0
        self.vertDictionary = {}

    def addVertex(self, n):
        self.num_vertices = self.num_vertices + 1
        newVertex = Vertex(n)
        self.vertDictionary[n] = newVertex
        return newVertex

    def addEdge(self,frm,to,cost=0):
        if(frm not in self.vertDictionary):
            self.addVertex(frm)
        if(to not in self.vertDictionary):
            self.addVertex(to)
        self.vertDictionary[frm].addNeighbour(self.vertDictionary[to], cost)
        # if it is an un-directed graph
        # self.vertDictionary[to].addNeighbour(self.vertDictionary[frm], cost)

    def getEdges(self, node):
        edges = []
        n = self.vertDictionary[node]
        conn =  n.getConnections()
        for item in conn:
            for key,value in self.vertDictionary.items():
                if value == item:
                    edges.append(key)
        return edges

if __name__ == '__main__':
    G = Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addVertex('d')
    G.addVertex('e')
    G.addEdge('a','b',4)
    G.addEdge('a','c',1)
    G.addEdge('c','b',2)
    G.addEdge('b','e',4)
    G.addEdge('c','d',4)
    G.addEdge('d','e',4)
    print G.getEdges('a')
