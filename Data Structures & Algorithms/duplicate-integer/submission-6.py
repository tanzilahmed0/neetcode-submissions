class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dupes = set(nums) 

        return False if len(dupes) == len(nums) else True