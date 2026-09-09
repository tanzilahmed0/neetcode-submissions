class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0 
        visited = set()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(row, col):
            if (row not in range(ROWS) or col not in range(COLS) or 
                grid[row][col] == '0' or (row, col) in visited): 
                return 
            
            visited.add((row, col)) 
            for dr, dc in dirs: 
                nr, nc = row + dr, col + dc
                dfs(nr, nc)

        for row in range(ROWS):
            for col in range(COLS): 
                if grid[row][col] == '1' and (row, col) not in visited: 
                    dfs(row, col) 
                    islands += 1
        

        return islands

        