class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # at each coin, we can either use the coin or not use it, but if we use it, that doesn't mean 
        # we can't not use it afterwards 
        # a brute force way would be to check every combination of coins that add up to amount and then 
        # return the minimum 
        # We can do a dynamic programming approach where we define dfs(i, amount) as the minimum 
        # number of coins to reach amount considering current coint 
        memo = [-1] * (amount + 1)

        def dfs(amount): 
            if amount == 0: 
                return 0 
            if memo[amount] != -1: 
                return memo[amount]
            take = float('inf')
            for coin in coins: 
                if amount - coin >= 0: 
                    take = min(1 + dfs(amount - coin), take)

            memo[amount] = take       
            return memo[amount]
        
        if dfs(amount) != float('inf'):
            return dfs(amount) 
        else: 
            return -1
                

