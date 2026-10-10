class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        # We can iterate through nums and use a set for O(1) look up
        # Basically if there's no number nums[i] - 1 in the set that means it can be the start of the
        # consecutive sequence and then we can update our max length 

        maxLength = 0
        setNums = set(nums) 

        for i in nums:
            if i-1 not in setNums: 
                length = 1
                while i+1 in setNums: 
                    length += 1 
                    i += 1 
                maxLength = max(maxLength, length)

        return maxLength