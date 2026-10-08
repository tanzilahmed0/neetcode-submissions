class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # So there can be either one partition or two partitions 
        # So a brute force approach would be to repeatedly try every possible partition/partitions 
        # point and see if the subsets are equal 
        total = sum(nums) 
        if total % 2 != 0:
            return False 
        half = total // 2 

        memo = {}
        def backtrack(i, currSum): 
            if currSum == half: 
                return True 

            if i == len(nums) or (i, currSum) in memo or currSum > half:              
                return False           
    
            result = (backtrack(i+1, currSum + nums[i])  or backtrack(i+1, currSum))

            if not result: 
                memo[(i, currSum)] = False 
            return result
                
        return backtrack(0, 0)
