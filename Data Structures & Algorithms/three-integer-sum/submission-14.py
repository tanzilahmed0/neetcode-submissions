class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        # We have an outer loop where we iterate through each value, where i is fixed
        # then and inner loop with 2 pointers, so we have 3 values to add up# 
        # if it adds up to 0, we add it to result
        result = []
        i =0 
        for i in range(len(nums)): 
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1 

            while l < r: 
                total = nums[i] + nums[l] + nums[r]

                if total < 0: 
                    l += 1 
                elif total > 0: 
                    r -= 1 
                else: 
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1 
                    r -= 1
                    while l < r and nums[l] == nums[l-1]: 
                        l += 1 
    

        return result

