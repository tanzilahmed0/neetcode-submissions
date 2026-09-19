from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # So we can do a multi source bfs from each rotten fruit
        # We can iterate through the grid and count the number of fresh fruit
        # and add any rotten fruit to the queue 
        # and then we can run a bfs where we enqueue any neighboring fresh fruit 
        # with it's current level, and every time we enqueue we decrease the number of fresh fruit 
        # at the end if the count is 0 we return the level, if not we return -1 
        # We need a level order bfs structure with a while loop 

        rows, cols = len(grid), len(grid[0]) 
        directions = [(1,0), (-1,0), (0,1), (0,-1)] 
        queue = deque() 
        minutes = 0 
        fresh = 0 

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 1: 
                    fresh += 1 
                if grid[r][c] == 2: 
                    queue.append((r,c))
        
        while queue and fresh > 0: 
            levelSize = len(queue) 
            for i in range(levelSize): 
                r, c = queue.popleft()
                for dr, dc in directions: 
                    nr, nc = r + dr, c + dc 
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        queue.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh -= 1 
            
            minutes += 1

        if fresh == 0: 
            return minutes 
        else: 
            return -1