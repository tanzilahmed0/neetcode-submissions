from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: 
            return 0 

        rows, cols = len(grid), len(grid[0]) 
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        fresh = 0 
        queue = deque()
        last = 0

        for r in range(rows):
             for c in range(cols): 
                if grid[r][c] == 2: 
                    queue.append((r, c, 0))
                elif grid[r][c] == 1: 
                    fresh += 1 
        if fresh == 0: 
            return 0


        while queue: 
            r, c, time = queue.popleft()
            last = time 
            for dr, dc in directions: 
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2 
                    queue.append((nr, nc, time + 1))
                    fresh -= 1
        
        if fresh != 0: 
            return -1 
        else: 
            return last

        
                    


        