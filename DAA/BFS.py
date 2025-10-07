class Graph:
    def __init__(self,num_vertices):
        self.num_vertices = num_vertices
        self.matrix = []
        for i in range(num_vertices):
            self.matrix.append([0] * num_vertices)
    
    def add_edge(self,i,f,weight = 1):
        if (((i< self.num_vertices) and (i>=0))and ((f<self.num_vertices)and(f>=0))):
            self.matrix[i][f] = weight
        else: print("vertix out of bount")

    
    def printMatrix(self):
        for i in self.matrix:
            print(i)
