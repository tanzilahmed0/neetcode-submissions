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
        memo = {}

        def dfs(remaining): 
            if remaining in memo: 
                return memo[remaining]

            if remaining == 0: 
                return 0 
            
            if remaining < 0: 
                return float('inf')

            min_cost = float('inf')
            for coin in coins: 
                result = dfs(remaining - coin)
                min_cost = min(min_cost, 1 + result)
            
            memo[remaining] = min_cost
            return min_cost

        result = dfs(amount) 
        if result == float('inf'): 
            return -1 
        else: 
            return result
