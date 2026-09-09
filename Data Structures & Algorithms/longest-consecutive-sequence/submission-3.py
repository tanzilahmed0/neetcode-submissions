class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        set_nums = set(nums) 

        max_length = 1

        # I need to check if num - 1 in set 
        for num in nums: 
            length = 1

            if num - 1 in set_nums:
                continue 

            else:
                while num + 1 in set_nums: 
                    length += 1 
                    num += 1
                    if length > max_length:
                        max_length = length
        
            
        return max_length