class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # At each index, we recursively decide whether we include that number to the subset or not 
        # After moving on we make that same decision for each number until we reach the end of the array
        # At each element there's 2 possible decisions so there's 2^n subsets with max size n 
        # So Time complexity is O(2^n * n), Space Complexity is O(n)

        result = []
        path = []

        def backtrack(i): 
            if i == len(nums): 
                result.append(path.copy())
                return 
            
            # This is the decision to include the current number 
            path.append(nums[i]) 
            backtrack(i+1)

            # This is the decision to NOT include the current numbers
            path.pop()
            backtrack(i+1)

        backtrack(0)
        return result

        