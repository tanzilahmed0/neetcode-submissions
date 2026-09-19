class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # Since we can only choose each element only once 
        # Our choice is to either include the next element or not 
        # So if our current target - sum < 0, we need to backtrack and move to next element 
        # if we reach target we add it to our result and then backtrack 
        # if we reach the end of candidates we also backtrack 

        result = [] 
        path = [] 
        candidates.sort()
        
        def backtrack(i, remaining):        
            if remaining == 0: 
                result.append(path.copy())
                return

            if  i == len(candidates) or remaining < 0: 
                return 
            
            

            # Choice 1 : Including this element or not 
            path.append(candidates[i])  
            backtrack(i + 1, remaining - candidates[i])

            # Choice 2: Not including this element, still move on to next one
            path.pop()
            while i+1 < len(candidates) and candidates[i+1] == candidates[i]: 
                i += 1     
            backtrack(i + 1, remaining)
            
        backtrack(0, target)
        return result


            
                

        
        