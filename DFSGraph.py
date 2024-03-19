from collections import defaultdict

# DFS traversal of provided Graph
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printGraph(self):
        print(self.graph)

    # run DFS using recursion
    def runDFS(self, v, visited):
        visited.add(v)
        print(f"visited node = {v}")
       
        # iterate through nbrs as you travel 
        # the tree from one node to each branch
        for nbr in self.graph[v]:
            if nbr not in visited:
                self.runDFS(nbr, visited)

# create the graph and run DFS
if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
 

    """ 
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(0,3)
    g.addEdge(2,3)
    g.addEdge(2,4)
    """ 
   
    g.printGraph()

    # run the dfs
    visited = set() 
    g.runDFS(2, visited) 
