class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # After u choose a coin, ur solving coin change again but for a different amount 
        # So at each branch, can choose 3 paths, and return the minimum cost at each path 
        # So dfs(remaining) will return the minimum coins to reach that amount that will 
        # return back up to the previous branch. 
        # If the remaining amount = 0, we've found one so we can return it
        # If it < 0 we return normally 
        # So dfs(0) should return 0
        # We have to compare the branches to see which one returns minimum cost so we return positive infinity
        #                      12 
        #   Take 1          Take 5           Take 10 
        #.     11              7                2
        #   Take 1 
        
        # Bottom Up Approach
        # dp would store the minimum amount of coins to make that amount 

        dp = [float('inf')] * (amount + 1) 
        dp[0] = 0 

        # [0, inf, inf]
        for i in range(1, len(dp)):
            amount = i 
            for coin in coins: 
                result = amount - coin
                if result < 0: 
                    continue

                dp[i] = min(dp[i], 1 + dp[result])
        
        if dp[-1] == float('inf'): 
            return -1 
        else: 
            return dp[-1]
                
                


