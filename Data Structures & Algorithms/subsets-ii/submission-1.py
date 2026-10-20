class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Normally, we can try ever
        #.                      []
        #.                  [1]       []
        #.          [1,2].      [1]        [2]       []
        # [1, 2, 1].  [1,2] [1,1] [1].  [2, 1] [2]. [1] []
        # We can sort nums so all duplicates will be next to each other 
        # [1, 1, 2] 
        # If we skip a number and the next digit is the same, we just skip that one too 

        #
        result = [] 
        path = [] 
        nums.sort()

        def backtrack(i): 
            if i == len(nums): 
                result.append(path.copy())
                return 
            
            # Take branch 
            path.append(nums[i]) 
            backtrack(i+1)

            # Skip branch 
            path.pop() 
            while i < len(nums) - 1 and nums[i+1] == nums[i]: 
                i += 1 
            backtrack(i+1) 

        backtrack(0)
        return result 