class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        # We can have a running sum but if we run in to a negative number, we check whether to extend the subarray
        # to include by getting the max of (currsum, currSum+nums[i])
        # If our running sum is negative, we start a new subarray at that index 

        result, currSum = nums[0], nums[0]

        for i in range(1, len(nums)): 
            if currSum < 0: 
                currSum = nums[i] 
            else: 
                currSum += nums[i]

            result = max(currSum, result)

        return result 

