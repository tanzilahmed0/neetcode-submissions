from collections import deque 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # We can traverse the grid with dfs or bfs and keep track of a running area 
        # and then after we call a bfs or dfs we update maxArea, we can have the bfs return the area 

        rows, cols = len(grid), len(grid[0]) 
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        maxArea = 0 

        def bfs(r, c): 
            queue = deque([(r, c)])  
            grid[r][c] = 0
            area = 0
            while queue: 
                row, col = queue.popleft()
                area += 1
                for dr, dc in directions: 
                    nr, nc = row + dr, col + dc 
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        grid[nr][nc] = 0

            return area

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 1: 
                    maxArea = max(maxArea, bfs(r, c))

        return maxArea
         