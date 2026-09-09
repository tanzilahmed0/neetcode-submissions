class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        check = {}

        for index, elem in enumerate(nums): 
            complement = target - elem 
            if complement in check: 
                return [check.get(complement), index] 
            else: 
                check[elem] = index

