class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Output can't contain duplicates 
        # We can sort the array and then use two pointers and hashmap 
        # We can have a left and right pointer, and have a as a fixed variable 
        # we can get a and i from enumerating over nums 
        # if nums[left] + nums[right] + a > or < 0, we move the pointers accordingly
        # we can have the left pointer immediately after a every time

        triplets = []

        nums = sorted(nums)     

        for i, a in enumerate(nums): 
            left, right = i + 1, len(nums) - 1 
            if i > 0 and a == nums[i-1]: 
                continue
            
            while left < right: 
                if nums[left] + nums[right] + a < 0: 
                    left += 1 
                elif nums[left] + nums[right] + a > 0: 
                    right -= 1
                elif nums[left] + nums[right] + a == 0: 
                    triplets.append([nums[left], nums[right], a])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                    while nums[right + 1] == nums[right] and right > left: 
                        right -=1

                    

        return triplets


        
        