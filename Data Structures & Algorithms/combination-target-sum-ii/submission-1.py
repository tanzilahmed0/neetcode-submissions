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
        # We sort the candidates because then any duplicate candidates are right next to each other 
        
        def backtrack(i, remaining):
            # If we find a correct subset, we add that to result        
            if remaining == 0: 
                result.append(path.copy())
                return
            # We check if we've reached the end of the array or exceed target and then backtrack
            if i == len(candidates) or remaining < 0: 
                return        

            # Choice 1 : Including this element or not 
            path.append(candidates[i])  
            backtrack(i + 1, remaining - candidates[i])

            # Choice 2: Not including this element, still move on to next one
            # We have to check if the next element is a duplicate, if is we move on to the next index 
            # Then run backtrack on the next index 
            path.pop()
            while i+1 < len(candidates) and candidates[i+1] == candidates[i]: 
                i += 1     
            backtrack(i + 1, remaining)
            
        backtrack(0, target)
        return result


            
                

        
        