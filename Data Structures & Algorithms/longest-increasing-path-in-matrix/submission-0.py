class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0]) 
        memo = {}
        directions = [(1,0), (-1,0), (0,-1), (0,1)]

        def dfs(r, c): 
            if (r, c) in memo: 
                return memo[(r,c)]
            
            longest = 1 

            for dr, dc in directions: 
                nr, nc = dr + r, dc + c 
                if (0 <= nr < rows) and (0 <= nc < cols) and matrix[nr][nc] > matrix[r][c]:
                    longest = max(longest, 1 + dfs(nr, nc))

            memo[(r, c)] = longest
            return longest

        result = 0 
        for r in range(rows):
            for c in range(cols): 
                result = max(result, dfs(r,c))
            
        return result

