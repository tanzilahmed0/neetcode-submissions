class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # recursion with memoization
        # At each step, we take the minimum cost of future step and store it

        n = len(cost)
        memo = {}

        def dfs(i): 
            # Base Case: Reaching the end of cost 
            if i >= n: 
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return memo[i]

        return min(dfs(0), dfs(1))


    
        
        

