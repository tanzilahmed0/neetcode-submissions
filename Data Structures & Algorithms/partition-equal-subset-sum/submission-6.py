class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # So essentially, we're trying to figure out if there's a subset that is equal to the target sum
        # which is half of the array 
        # At each index, we have the choice of either choosing to include it as part of our subset or not
        # 

        if sum(nums) % 2 != 0: 
            return False 
        
        half = sum(nums) // 2 
        dp = {0}

        for i in range(len(nums)): 
            nextDP = set()
            for j in dp: 
                # we take the current value 
                nextDP.add(j + nums[i])
                # We skip the current value 
                nextDP.add(j)
            dp = nextDP
        return half in dp
        
