class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # we want to find the numbers that can start a sequence, 
        # we can turn into a set for constant look up  

        result = 1
        set_nums = set(nums)
        
        if not nums: 
            return 0 

        for i in nums: 
            count = 0 
            if i >= 0 and i-1 in set_nums: 
                continue 
            else: 
                count += 1
                while i + 1 in set_nums: 
                    count += 1 
                    i += 1 
                    result = max(result, count)

        return result



       

        