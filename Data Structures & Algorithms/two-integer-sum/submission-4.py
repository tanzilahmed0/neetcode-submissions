class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {} 
        result = []

        for i, val in enumerate(nums): 
            complement = target - val
            if complement in count: 
                result.append(count[complement])
                result.append(i)
                
            count[val] = i

        return result


