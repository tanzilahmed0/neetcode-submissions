class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # We can define dp[i] on if we can reach that index from 0

      
        # Wait we can just iterate through the array and keep track of the farthest index we can reahc which is 
        # i + nums[i]
        n = len(nums)
        result = 0
        # [True, True, True, True,]
        i = 0
        while i < n - 1:
            if i > result:
                return False
            result = max(result, nums[i] + i)
            
            i += 1

   
        return result >= n - 1
            