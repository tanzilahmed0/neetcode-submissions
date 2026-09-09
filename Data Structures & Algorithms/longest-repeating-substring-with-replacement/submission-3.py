class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Constraint: The window has to be valid 
        # A window is valid if window length - count of most freq char <= k
        # In other words the # of chars to change has to be <= k
        # We need a hashmap to count the frequencies of the characters
         # We move the right pointer as long as it satisfies those constraints
         # if it doesn't we move the left pointer 
        
        left = 0 
        result = 1 

        strings = {} 

        for r in range(len(s)): 
            w_length = r - left + 1 
            strings[s[r]] = strings.get(s[r], 0) + 1 

            max_freq = max(strings.values())
            while w_length - max_freq > k:
                strings[s[left]] = strings.get(s[left], 0) - 1 
                left +=1
                w_length = r - left + 1 


            result = max(w_length, result)



        return result

            

            
                
            