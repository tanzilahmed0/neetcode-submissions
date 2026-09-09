class Solution:
    def findMin(self, nums: List[int]) -> int:
        new_nums = set(nums)

        return min(new_nums)
        