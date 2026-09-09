from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
        directions = [(1,0), (-1,0), (0,-1), (0,1)]
        queue = deque()

        def bfs(r, c):
            queue.append((r, c))
            visited.add((r,c))
            area = 0
            while queue: 
                r, c = queue.popleft()
                area += 1 
                for dr, dc in directions: 
                    nr, nc = r + dr, c + dc 
                    if ((0 <= nr < rows) and (0 <= nc < cols) and 
                        grid[nr][nc] == 1 and (nr, nc) not in visited): 
                        visited.add((nr,nc))
                        queue.append((nr, nc))
                              
            return area 


        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 1 and (r,c) not in visited: 
                    maxArea = max(maxArea, bfs(r, c))
        
        return maxArea