# number of islands in matrix
def numIslands(grid: list[list[int]]):
   
    def dfs(row, col):
        for dx,dy in directions:
            next_row, next_col = row+dy, col+dx
            if valid(next_row, next_col) and (next_row, next_col) not in seen:
                seen.add((next_row, next_col))
                dfs(next_row, next_col)

    def valid(row, col):
        return 0 <= row < M and 0 <= col < N and grid[row][col] == "1"

    # directions sides and top/bot
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    seen = set()
    ans = 0
    
    M = len(grid)
    N = len(grid[0])
    for row in range(M):
        for col in range(N):
            if grid[row][col] == "1" and (row,col) not in seen:
                ans += 1
                seen.add((row,col))
                dfs(row,col)

    return ans

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print("Grid:")
print(grid)
print("\n")

num_islands = numIslands(grid)
print(f"Nums = {num_islands}")
