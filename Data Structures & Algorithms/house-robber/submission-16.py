class Solution:
    def rob(self, nums: List[int]) -> int:
        

        # At each house we have a choice to either rob it or skip it 
        # dp[i] represents the max money u can get based on the previous i
        # at each index, u can either get dp[i-1] or dp[i-2] + nums[i]
        if len(nums) < 2: 
            return nums[0]

        dp = [0] * len(nums)
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)): 
            dp[i] = max(dp[i-1], (dp[i-2] + nums[i]))

        
        return dp[-1]