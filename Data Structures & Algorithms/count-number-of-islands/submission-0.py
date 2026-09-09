from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0 

        rows, cols = len(grid), len(grid[0])
        visited = set() 
        islands = 0 
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # When we find a new start, "1" not visited, we enqueue it 
        # and immediately start bfs 
        def bfs(r, c): 
            queue = deque()
            # We added it to visited then add it to the queue 
            visited.add((r, c))
            queue.append((r, c))
            
            while queue: 
                row, col = queue.popleft()
                # for that 1, we check all directions to see if there's a 1 that's 
                # not visited, if we find one, we add it to the queue then add it 
                # to visited 
                for dr, dc in directions: 
                    r, c = row + dr, col + dc
                    if (r in range(rows) and 
                        c in range(cols) and 
                        grid[r][c] == '1' and 
                        (r, c) not in visited): 
                        queue.append((r, c)) 
                        visited.add((r, c))


        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == '1' and (r, c) not in visited: 
                    # Increment islands by 1 when we find a new "1"
                    bfs(r, c)
                    islands += 1
                
        

        return islands
