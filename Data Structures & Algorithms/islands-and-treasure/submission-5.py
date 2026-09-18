from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # What we can do is when we encounter a treasure chest, we run a bfs to each cell 
        # that stores the running distance, so neighoring cells would be 1, we modify it in place 
        # 
        
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0, 1), (0,-1)] 
        INF = 2147483647

        queue = deque() 

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 0: 
                    queue.append((r, c, grid[r][c]))

 

        while queue: 
            r, c, distance = queue.popleft()
                
            for dr, dc in directions: 
                nr, nc = r + dr, c + dc 
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF: 
                    queue.append((nr, nc, distance + 1))
                    # Must mark the cell as visited when you enqueue it, not when you dequeue it, 
                    # so another BFS path can't enqueue it again because BFS naturally finds shortest path 
                    # so if it has already been modified we know it's the shortest path 
                    grid[nr][nc] = distance + 1 
                    
                    