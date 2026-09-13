from collections import Counter 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # We can think of a permutation of a string like an anagram, so it will have the same 
        # freq counts. What we can do is have a sliding window of size len(s1) that 
        # we move and update frequency counts, if they're equal at any point, we return true 
        # If we reach the end of the loop we return false. 

        s1Count = Counter(s1) 
        left = 0
        s2Count = Counter(s2[left:len(s1)])
        print(s2Count)

        if len(s1) > len(s2):
            return False
        
        if s2Count == s1Count: 
                return True  

        for right in range(len(s1), len(s2)):                 
            s2Count[s2[left]] -= 1 
            if s2Count[s2[left]] == 0: 
                del s2Count[s2[left]]
            s2Count[s2[right]] = s2Count.get(s2[right], 0) + 1
            left += 1
            if s2Count == s1Count: 
                return True  
    
        return False

        # for right in range(len(s2)): 


        