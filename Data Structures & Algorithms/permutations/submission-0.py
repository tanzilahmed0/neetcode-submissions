class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # So at the first index i have n choices 
        # at each iteration I have n-1 digits to choose from 
        # Each permutation is of length n
        # so each path can start of as [0] * len(nums) 
        # and then at each index we try every possible digit in nums 

        output = []
        perm = []
        used = set()


        def backtrack(): 
            # We've found a permutation
            if len(perm) == len(nums): 
                output.append(perm.copy())
                return 

            for num in nums: 
                if num in used: 
                    continue 
                # Choice 1: Use the current num at this index in perm 
                perm.append(num) 
                used.add(num)
                backtrack()

                # Choice 2: Don't use the current num and move on
                perm.pop()
                used.remove(num)
                # We don't call backtrack again because for loop already moves on to next possibility
                 
        backtrack()
        return output
