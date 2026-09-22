class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # when we start, we have choice of starting at index 0 or 1 
        # then we can either step to i+1 or i+2 floor
        # so I guess to think about it a brute force appraoch would be to recursively calculate the cost of each 
        # going from each step to the end and then updating 
        # We can memoize by storing the minim cost to reach each step 
        # so for example the minimum cost to reach 0 and 1 is 0 because we can start from there ]
        # Then to reach index 2 it's 1 because u can move 2 steps from index 0
        
        # Essentially, at each index starting from 2, I calculate the minimum cost of the 2 steps before it 
        # because that's the step that i'm going to take to get to my current step and then add the cost 
        # of the path i picked 
        n = len(cost) + 1
        dp = [0] * n
        dp[0], dp[1] = 0, 0

        for i in range(2, n):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[n-1]
        

