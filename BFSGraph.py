from collections import defaultdict, deque

# Graph class using adjacency list
class Graph:
    def __init__(self):
        # initialize dict with list for values 
        self.adjList = defaultdict(list)
       
    def addEdge(self, u, v):
        self.adjList[u].append(v)

    def printContent(self):
        print(self.adjList)

    def runBfs(self, startNode):
        # create queue
        queue = deque()
        visited = [False] * (max(self.adjList.keys()) + 2) 
        print("Visited:")
        print(visited)
        print("\n")

        # mark the current node as visted and enqueue it
        visited[startNode] = True
        queue.append(startNode)

        # iterate over the queue
        print("queue:") 
        while queue:
            # dequeue a vertex
            currNode = queue.popleft()
            print(currNode, end=" ")

            # get all nbr vertices - if adjacent not visted
            # then mark it visited and enqueue it
            print(f"nbrs len = {len(self.adjList[currNode])}") 
            for nbr in self.adjList[currNode]:
                print(f"nbr = {nbr}") 
                if not visited[nbr]:
                    visited[nbr] = True
                    queue.append(nbr)
            

# add edges to graph
graph = Graph()
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 3)
graph.addEdge(1, 2)
graph.addEdge(2, 4)
graph.addEdge(3, 4)

print("graph:")
graph.printContent()
print("\n")
graph.runBfs(0)
