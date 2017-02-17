class Vertex:
    def __init__(self,node):
        self.id = node
        self.visited = False

    def setvertexId(self,id):
        self.id = id

    def getVertexId(self):
        return self.id


class Graph:
    def __init__(self, numVertices, count = 0):
        self.adjMatrix = [[-1]*numVertices for i in range(numVertices)]
        self.numVertices = numVertices
        self.vertices = []
        for x in range(self.numVertices):
            newVertex = Vertex(x)
            self.vertices.append(newVertex)

    def printMatrix(self):
        import numpy as np
        print np.matrix(self.adjMatrix)

    def setVertex(self, vtx , id):
        if(vtx >= 0 and vtx < self.numVertices):
            self.vertices[vtx].setvertexId(id)

    def getVertex(self, n):
        for x in range(self.numVertices):
            if n == self.vertices[x].getVertexId():
                return x
        return -1

    def addEdge(self,frm,to,cost=0):
        if((self.getVertex(frm) != -1) and (self.getVertex(to) != -1)):
            self.adjMatrix[self.getVertex(frm)][self.getVertex(to)] = cost
            # For undirected graphs
            # self.adjMatrix[self.getvertex(to)][self.getvertex(from)] = cost

G = Graph(5)
G.setVertex(0, 'a')
G.setVertex(1, 'b')
G.setVertex(2, 'c')
G.setVertex(3, 'd')
G.setVertex(4, 'e')
G.addEdge('a','e',10)
G.addEdge('a','c',20)
G.addEdge('c','b',30)
G.addEdge('b','e',40)
G.addEdge('e','d',50)
G.addEdge('f','e',60)
G.printMatrix()
