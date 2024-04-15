from collections import defaultdict

# count the number of provinces/nodes in the graph
def findNumberNodes(isConnected: list[list[int]]) -> int:

    # dfs for neighbors
    def dfs(node):
        for nbr in graph[node]:
            # next lines prevent cycles
            if nbr not in seen:
                seen.add(nbr)
                dfs(nbr)

    # build the graph
    N = len(isConnected)
    graph = defaultdict(list)
    for i in range(N):
        print(f"i = {i}") 
        for j in range(i+1, N):
            print(f"j = {j}") 
            # find the 1 in the graph
            if isConnected[i][j]:
                graph[i].append(j)
                graph[j].append(i)

    print("Graph:")
    print(graph)
    print("\n")

    seen = set()
    ans = 0
    for i in range(N):
        if i not in seen:
            print(f"i = {i} not in seen") 
            print("seen:")
            print(seen)
            print(f"ans = {ans}") 
            print("\n")

            # add all nodes of a connected component to set
            ans += 1
            seen.add(i)
            dfs(i)

    return ans

#isConnected = [[1,1,0], [1,1,0],[0,0,1]]
isConnected = [[1,0,0], [0,1,0],[0,0,1]]
res = findNumberNodes(isConnected)
print(f"res = {res}")
