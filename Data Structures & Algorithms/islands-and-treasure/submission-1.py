from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # A more optimal approach is thinking inversely 
        # Instead of calculating distance from each land cell to 
        # each treasure, we can calculate the distance from each treasure chest
        # Since we're running the algorithm simultatenuously at each 
        # treasure chest, we're guaranteed to get the smallest distance 

        rows, cols = len(grid), len(grid[0]) 
        directions = [(1, 0), (-1,0), (0,1), (0,-1)]
        INF = 2147483647
        queue = deque()

        for r in range(rows):
            for c in range(cols): 
                if grid[r][c] == 0: 
                    queue.append((r,c))

        while queue: 
            r, c = queue.popleft()
            for dr, dc in directions: 
                nr, nc = r + dr, c + dc 
                if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == INF:
                    queue.append((nr,nc))
                    grid[nr][nc] = 1 + grid[r][c]
        