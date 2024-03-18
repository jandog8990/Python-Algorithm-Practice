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

    def findLevel(self, startNode, searchNode):
        queue = deque()
        vals = self.adjList.values()

        # loop through the vals and append to queue
        nodes = [v for vv in vals for v in vv]
        visited = [False] * (len(nodes)+1)

        visited[startNode] = True
        queue.append(startNode)

        level = 0 
        while queue:
            lidx = len(queue) 
            
            # first go through all values in the curr queue
            while (lidx > 0):
                currNode = queue.popleft()
                print(f"currNode = {currNode}") 
                nbrs = self.adjList[currNode]
                print(f"nbrs = {nbrs}") 
                print(f"level = {level}") 
                if currNode == searchNode:
                    print("nbr = {searchNode}")
                    print(f"level = {level}")
                    return level

                for nbr in nbrs:
                    if not visited[nbr]: 
                        visited[nbr] = True
                        queue.append(nbr)
                    print("Queue:") 
                    print(queue) 
                    print("\n") 
                lidx = lidx - 1 
            level = level + 1 
            print("\n")
        
        print("final queue:")
        print(queue)
        print("\n")
        return -1

# add edges to graph
graph = Graph()
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 3)
graph.addEdge(2, 4)

print("graph:")
graph.printContent()
print("\n")
level = graph.findLevel(0, 3)
print("final level for 3:")
print(level)
print("\n")

