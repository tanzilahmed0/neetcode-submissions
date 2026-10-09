class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # For permutations, we must return all possible orderings of all digits in nums 
        # So essentially at each index, i have n choices, then n-1 choices etc
        # We can write a backtracking algorithm that will exhaust all possible permutations 
        # At each index we have a choice of using it or not 
        # once we've added a number to the permutation, we can add it to a used set() 
        # so we can consider the other elements 
        # When we backtrack we pop it from set so we can consider the other elements 
        used = set()
        path = []
        result = []

        def backtrack(): 
            if len(path) == len(nums): 
                result.append(path.copy()) 
                return 

            for num in nums: 
                if num not in used: 
                    path.append(num)
                    used.add(num)
                    backtrack()

                    path.pop()
                    used.remove(num)
                  
        backtrack()
        return result


            



