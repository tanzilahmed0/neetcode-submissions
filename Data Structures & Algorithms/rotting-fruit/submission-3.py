from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # We can think of the rotten fruit as start nodes 
        # we can do bfs on them level by level and turn each fruit rotten 
        # First we need to know where the rotten fruit exactly are in the grid
        # We also need to track the fresh fruit to know if all of them are gone 
        # by the time we finish running our bfs. 
        # BFS overview: 
        # We'll enqueue every rotten fruit. 
        # We pop the rotten fruit from the queue, and check all of its neighbors. 
        # check for bounds and if it is a fresh fruit. Since we're only looking for fresh
        # fruit there is no need for a visited cells set.
        # Once we enqueue a fresh fruit, we decrement the fresh fruit count by 1,
        # and immediately make it rotten so we don't enqueue it again. 
        # We can enqueue each fruit with a time parameter that starts at 0
        rows, cols = len(grid), len(grid[0])
        directions = [(1 , 0), (-1 , 0), (0 , 1), (0 ,-1)]
        queue = deque([])
        fresh = 0
        time = 0

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 2: 
                    queue.append((r, c, time))
                elif grid[r][c] == 1: 
                    fresh += 1
        print(queue)
        while queue: 
            r, c, time = queue.popleft()
            for dr, dc in directions: 
                nr, nc = r + dr, c + dc
                if ((0 <= nr < rows) and (0 <= nc < cols) and 
                    grid[nr][nc] == 1): 
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, time + 1))

        if fresh == 0: 
            return time
        else: 
            return -1





        