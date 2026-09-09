from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # First we need to go through the whole grid, and find which fruits are rotten
        # Then we add to the queue.
        # Dfs is not guaranteed to return the minimum path 
        # We also need to keep track of the number of fresh fruit 
        # We can say that once we add each fruit's neighbors to the queue 
        # We increment minutes by 1 

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        fresh = 0 
        time = 0

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 2: 
                    queue.append((r,c, 0))
                if grid[r][c] == 1: 
                    fresh += 1
        
        while queue: 
            r, c, time = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == 1: 
                    grid[nr][nc] = 2
                    queue.append((nr, nc, time + 1))
                    fresh -= 1 
                
        if fresh == 0:
            return time
        else: 
            return -1
      
        