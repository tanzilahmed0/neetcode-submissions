class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # This question is asking for the indices of two digits
    # in the array that add up to the given target value
    # This is a sliding window problem 

    # Brute Force solution
        for i in range(len(nums)): 
            for j in range(i+1,len(nums)): 
                if nums[i] + nums[j] == target: 
                    return [i, j] 
            