class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # We can define dp[i] on if we can reach that index from 0

        dp = [False] * len(nums)
        dp[0] = True 
        
        # [True, True, True, True,]
        for i in range(len(nums)): 
            if dp[i] == True: 
                for j in range(i+1, i + nums[i] + 1):
                    if j < len(nums):
                        dp[j] = True 

        
        return dp[-1]