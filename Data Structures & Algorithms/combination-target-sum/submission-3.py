class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # At each candidate, we have two choices, add it to current sum or not 
        # We need to check if we've reached out of bounds or our sum exceeds target 
        # if we've reached target, we add to result and immediately pop our decision
        # If we decide to add that number, we recursively backtrack and subtract from our target

        result = [] 
        combs = [] 
        
        def backtrack(i, remaining): 
            if i >= len(nums) or remaining < 0:
                return 
            # If target is found, we add the current number, and add that subset to result 
            # We need to undo this choice right after and return to previous decision
            if remaining == 0: 
                result.append(combs.copy())
                return 
            
             
            # Choice 1: Including this current number 
            combs.append(nums[i])
            backtrack(i, remaining - nums[i])

            # choice 2: Not including this current number and moving on, so the target shouldn't change
            combs.pop()
            backtrack(i+1, remaining)

        backtrack(0, target)
        return result