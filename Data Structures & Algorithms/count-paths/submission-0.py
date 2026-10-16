class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # We can think of this as the number of possible ways you can reach that square previously 
        # So we can initialize dp[m][i] which is equal to dp[m-1][i] + dp[m][i-1]

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0: 
                    continue 
                
                if 0 <= r-1 < m: 
                    dp[r][c] += dp[r-1][c]
                
                if 0 <= c-1 < n:
                    dp[r][c] += dp[r][c-1]

        
        return dp[m-1][n-1]