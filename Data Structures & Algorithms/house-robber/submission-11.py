class Solution:
    def rob(self, nums: List[int]) -> int:

        # We can just have a bottom up approach where 
        # we initialize a dp array of size n, where dp[0] = nums[0] and dp[1] = nums[1]  
        # Then we can iterate through 2 to the end of nums and then say dp[i] = dp[i-2] + nums[i]  
        # and then return the max of n-1 and n-2
        # But at each house i, we can either rob the house or not rob it 

        n = len(nums) 
        # dp stores the maximum amount of money so far I could've robbed at that house
        dp = [0] * n
        if n < 2: 
            return nums[0]
        dp[0] = nums[0] 
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n): 
            # Two choices, rob the current house or skip it 
            # If I rob it, it's the money from the house 2 indices ago + current amount
            # If i don't, my money is the amount from the last house
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        return max(dp)