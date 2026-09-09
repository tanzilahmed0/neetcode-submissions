class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0,-1)]
        # We need 2 sets to check which cells are able to reach both
        pacific = set()
        atlantic = set()
        output = []

        def dfs(r, c, ocean, prev_height): 
            if ((not 0 <= r < rows) or not (0 <= c < cols) or 
                (r,c) in ocean or heights[r][c] < prev_height): 
                return 
            # We recursively check if every neighboring cell is also able to reach 
            # the ocean
            ocean.add((r, c)) 
            for dr, dc in directions: 
                nr, nc = r + dr, c + dc 
                dfs(nr, nc, ocean, heights[r][c])

        # We run dfs on both of the borders, and see which nodes are able to reach it
        # basically doing it in reverse order. Then we add it to a set 
        for c in range(cols): 
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])
        for r in range(rows): 
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        # We return the intersection of both sets 
        result = pacific & atlantic
        return [list(i) for i in result]

            


