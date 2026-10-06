class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # So at each index, we have the choice of using that element or not using that element
        result = [] 
        path = []
        nums.sort()

        def backtrack(i): 
            if i == len(nums): 
                result.append(path.copy())
                return 
            
            path.append(nums[i]) 
            backtrack(i+1) 

            path.pop()
            while i < len(nums) - 1 and nums[i+1] == nums[i]:
                i += 1 
            backtrack(i+1)

        backtrack(0)
        return result
