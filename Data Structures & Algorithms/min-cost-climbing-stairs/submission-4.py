class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        # So at each step, the minimum cost to reach it, is the min cost of the 2 steps 
        # right before it 
        # So dp represents, the min cost to reach that step, and then when u take the next step u add cost[i]
        # [1,2,1,2,1,1,1] 
        # [0,0,1,2,2,3,3,4]

        dp = [0] * (len(cost) + 1)

        dp[0], dp[1] = 0, 0 

        for i in range(2, len(cost) + 1): 
            dp[i] = min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2])

        return dp[-1]
    