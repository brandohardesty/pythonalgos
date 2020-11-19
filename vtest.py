class Graph:
    adjMat = list(list())
    def __init__(self,verticies,edges):
        self.verticies = verticies
        self.edges = edges
        self.adjMat = list(list())
        for i in range(0,len(self.verticies)):
            self.adjMat.append([0 for j in range(0,len(self.verticies))])


    def addVertex(self,value,friends):
        self.verticies.append(value)
        for i in friends:
            self.edges.append((value,i))
    def testMat(self):
        self.adjMat[0][1] = 10
        print(self.adjMat)
    def genAdjMatrix(self):
        for i in range(0,len(self.verticies)):
                for j in range(0,len(self.verticies)):

                    if((i,j) in self.edges):
                        print(i,j)
                        print((i,j) in self.edges)
                        self.adjMat[i][j] = 1
                        self.adjMat[j][i] = 1
                    else:
                        print(i,j)
                        print((i,j) in self.edges)


    



v = [0,1,2]
e = [(0,1),(0,2)]
g = Graph(v,e)
g.testMat()
g.genAdjMatrix()
print(g.adjMat)
print("test")
