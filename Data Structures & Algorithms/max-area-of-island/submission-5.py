class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # We can run dfs whenever we see a 1 we haven't visited before 
        # and whenever we visit an adjacent one, we increase the area by one 
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        maxArea = 0 

        def dfs(r, c): 
            if ((not 0 <= r < rows) or (not 0 <= c < cols) or (r,c) in visited or grid[r][c] == 0):
                return 0 

            area = 1 
            visited.add((r,c))
            for dr, dc in directions: 
                nr, nc = r + dr, c + dc 
                area += dfs(nr, nc)

            return area 



        for r in range(rows): 
            for c in range(cols): 
                if (r,c) not in visited and grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r,c))

        return maxArea