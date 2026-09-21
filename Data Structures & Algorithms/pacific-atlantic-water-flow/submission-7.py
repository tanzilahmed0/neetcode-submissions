class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:


        # we can have 2 sets, pacific and atlantic which stores the adjacent cells 
        # And then from each cell in the pacific, we see if we can reach the cells that 
        # are in the atlantic ones because if they are, we know they reach the atlantic ocean 
        # because all adjacent cells reach them, 
        # Essentially we run dfs from the pacific side and see which cells reach atlantic 
        # and then re run dfs from atlantic side and see which cells reach pacific 

        pacific, atlantic = set(), set() 
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, ocean): 
            ocean.add((r, c))           
            for dr, dc in directions: 
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in ocean and heights[nr][nc] >= heights[r][c]: 
                    dfs(nr, nc, ocean)

        for c in range(cols): 
                dfs(0, c, pacific)
                dfs(rows - 1, c, atlantic) 
        for r in range(rows):
                dfs(r, 0, pacific)
                dfs(r, cols-1, atlantic)

        return list(pacific & atlantic)

            
