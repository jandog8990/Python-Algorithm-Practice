from collections import defaultdict

# program to count the islands in a 2D matrix
# where an island is a group of connected 1s
# separated by 0s that separate each island
class IslandGraph:
    def __init__(self, row, col, graph):
        self.ROW = row
        self.COL = col
        self.graph = graph

    def isSafe(self, i, j, visited):
        # isSafe method to check if current vertex is 1 AND NOT visited
        # and that it's within the boundaries of main matrix
        return (i >= 0 and i < self.ROW and
            j >= 0 and j < self.COL and
            not visited[i][j] and (self.graph[i][j] == 1))

    def DFS(self, i, j, visited):
        # DFS for 2D matrix, 8 nbrs of current vertex
        # note that rows and cols are indices of the nbrs
        rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]

        # mark the current cell as visited
        visited[i][j] = True

        # recursion for the other connected nbrs
        for k in range(len(rowNbr)):
            # check to see if the current nbr is 1 and NOT visited 
            kRowNbr = i + rowNbr[k]
            kColNbr = j +colNbr[k]
            if self.isSafe(kRowNbr, kColNbr, visited):
                # re-run the DFS algo to check for nbr's nbrs
                return self.DFS(kRowNbr, kColNbr, visited)

    def countIslands(self):
        # initialize the visited matrix with F 
        visited = [[False for j in range(self.COL)] 
            for i in range(self.ROW)]
        print(visited)

        # initialize the island count and traverse
        # the given matrix and find the 1s
        # I AM THE ONE
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # if cell is 1 and not visited
                # then this is a new island
                if visited[i][j] == False and self.graph[i][j] == 1:
                    # visit all cells in this island
                    # does this include nbr calculation?
                    # increment island count for each 1 found
                    self.DFS(i, j, visited)
                    count = count + 1
 
        # return the total count of islands
        return count

mat = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0]]
row = len(mat)
col = len(mat[0])
graph = IslandGraph(row, col, mat)

numIslands = graph.countIslands()
print(f"Num islands = {numIslands}")
