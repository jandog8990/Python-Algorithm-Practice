from collections import deque,defaultdict

# check if given source/destination creates a path
def validPath(N: int, edges: list[list[int]], source: int, destination: int) -> bool:
    # store edges in graph
    graph = defaultdict(list)
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # store all nodes visited in queue
    seen = [False]*N
    seen[source] = True
    queue = deque([source])

    while queue:
        curr_node = queue.popleft()
        if curr_node == destination:
            return True

        # for all nbrs of curr node, if not visited
        # add it to 'queue' and mark as visited
        for next_node in graph[curr_node]:
            if not seen[next_node]:
                seen[next_node] = True
                queue.append(next_node)

    return False
