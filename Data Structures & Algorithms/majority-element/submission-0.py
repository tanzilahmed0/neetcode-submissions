from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freqs = Counter(nums)
        n = len(nums) 

        for key, value in freqs.items(): 
            if value > n // 2: 
                return key
        

        