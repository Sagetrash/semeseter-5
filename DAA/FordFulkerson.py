from collections import defaultdict

class Graph:
    def __init__(self,graph):
        self.graph = graph
        self.row = len(graph)

    def BFS(self,s,t,parent):  # function to perform BFS
        visited = [False]*(self.row)
        queue = []
        queue.append(s)
        visited[s]=True

        while queue :
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
        return False
        
    def fordFulkerson(self,source,sink):
        parent = [-1]*(self.row)
        max_flow = 0 # zero initial flow
        while self.BFS(source,sink,parent):
            path_flow = float("inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow,self.graph[parent[s]][s])
                s = parent[s]
            
            max_flow += path_flow
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow
    
graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]

g = Graph(graph)
print(g.fordFulkerson(0,5))