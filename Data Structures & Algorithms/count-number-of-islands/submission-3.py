class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0]) 
        visited = set()
        directions = [(1, 0), (-1,0), (0, 1), (0, -1)]
        islands = 0

        if not grid or not grid[0]:
            return 0

        def dfs(r, c): 
            if (not (0 <= r < rows) or not (0 <= c < cols) or
                grid[r][c] == '0' or (r,c) in visited):
                return 
            visited.add((r,c))

            for dr, dc in directions: 
                nr, nc = r + dr, c + dc
                dfs(nr, nc)


        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r, c) 
                    islands += 1
        
        return islands