class Solution:
    def climbStairs(self, n: int) -> int:
        

        # The number of ways to reach the top is basically the sum of the number of distinct ways 
        # of the previous 2 steps 

        if n <= 2: 
            return n 

        dp = [0] * n 
        dp[0], dp[1] = 1, 2 

        for i in range(2, n): 
            dp[i] = dp[i-1] + dp[i-2] 

        
        return dp[n-1]