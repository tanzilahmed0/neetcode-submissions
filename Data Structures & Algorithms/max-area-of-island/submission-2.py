from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Let's do it with BFS 
        rows, cols = len(grid), len(grid[0]) 
        visited = set()
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        maxArea = 0

        def bfs(r, c): 
            # We need to check if the current cell is valid, if it's not 
            # the area is 0
            if (r not in range(rows) or c not in range(cols)
                or grid[r][c] == 0 or (r,c) in visited): 
                return 0
            # Since it's valid, we enqueue in and add it to the visited set
            queue = deque([(r,c)])
            visited.add((r, c)) 
            area = 0 
            while queue: 
                # We pop the current cell, and increment area by 1
                r, c = queue.popleft()
                area += 1 
                for dr, dc in directions: 
                    # We check all directions of the cell, if they're valid 
                    # we enqueue in then add it to visited 
                    nr, nc = r + dr, c + dc 
                    if (nr in range(rows) and nc in range(cols) and
                    grid[nr][nc] == 1 and (nr, nc) not in visited):
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            return area 


        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 1 and (r, c) not in visited: 
                    maxArea = max(maxArea, bfs(r, c))

        return maxArea
        