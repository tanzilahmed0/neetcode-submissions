class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numbers = {}    

        for index, n in enumerate(nums): 
            complement = target - n 

            if complement in numbers: 
                return [numbers[complement], index]
            else: 
                numbers[n] = index
            
        
