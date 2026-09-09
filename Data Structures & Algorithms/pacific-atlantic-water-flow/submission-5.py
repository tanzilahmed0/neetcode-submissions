class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Instead of thinking of which cells reach both oceans 
        # We can think backwards and think which ones reach atlantic from 
        # pacific and vice versa 
        # The cells on the borders automatically visit both the pacific
        # and the atlantic
        # if we run a dfs from the pacific border cells to see which ones 
        # they can visit and put them into pacific set
        # and then do the same with atlantic 
        # the cells that are in both sets can reach both oceans 
        # First we need to get the border cells 
        # We also need to keep track of the previous height
        pacific, atlantic = set(), set () 
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(heights), len(heights[0])
        output = []

        def dfs(r, c, ocean, prevHeight): 
            if ((not 0 <= r < rows) or (not 0 <= c < cols) or (r,c) in ocean
                or heights[r][c] < prevHeight): 
                return 
            ocean.add((r, c))
            for dr, dc in directions: 
                nr, nc = r + dr, c + dc
                dfs(nr, nc, ocean, heights[r][c])

        for c in range(cols): 
            dfs(0, c, pacific, heights[0][c]) 
            dfs(rows-1, c, atlantic, heights[rows-1][c])

        for r in range(rows): 
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols-1, atlantic, heights[r][cols-1])
        
        for r in range(rows): 
            for c in range(cols): 
                if (r, c) in pacific and (r, c) in atlantic: 
                    output.append([r,c])
        
        return output
            
        