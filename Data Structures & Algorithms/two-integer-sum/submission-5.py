class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for idx, val in enumerate(nums): 
            if target - val in complements: 
                return [complements[target-val], idx]
            complements[val] = idx