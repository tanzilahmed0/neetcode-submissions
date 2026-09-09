class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums) 

        prefix = 1
        for i in range(len(nums)): 
            # The first element prefix is always one, so we start it at that
            result[i] = prefix
            # then we multiply prefix by the current number for the next one
            prefix *= nums[i] 
        postfix = 1 
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i] 
        
        return result
 

        

        