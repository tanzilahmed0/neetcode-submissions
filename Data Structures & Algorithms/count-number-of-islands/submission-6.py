class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # So what we can do is go through each cell and when we encounter a 1, we recursively visit 
        # all of it's neighbors that are ones and that increment the count of islands by 1 

        islands = 0 
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)] 
        visited = set() 

        def dfs(r, c): 
            if (not 0 <= r < rows) or (not 0 <= c < cols) or grid[r][c] != '1' or (r,c) in visited: 
                return
            visited.add((r,c))     
            for dr, dc in directions: 
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
            

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == '1' and (r,c) not in visited: 
                    dfs(r,c) 
                    islands += 1 

        return islands
