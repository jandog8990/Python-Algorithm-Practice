from collections import defaultdict

# building a graph using a dict of lists
def build_graph(edges: list[list[int]]) -> defaultdict:
    graph = defaultdict(list)
    for x,y in edges:
        # directed
        graph[x].append(y)
        # undirected
        #graph[y].append(x)

    return graph

x = [[0,1],[1,2],[2,0],[2,3]]
graph = build_graph(x)
print("Graph:")
print(graph)
print("\n")
