class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l1 = len(s1) 
        l2 = len(s2) 

        s1count = {}
        s2count = {} 

        if l1 > l2: 
            return False

        # Getting the frequencies of string 1 and the first window
        for ch in range(l1): 
            s1count[s1[ch]] = s1count.get(s1[ch], 0) + 1 
            s2count[s2[ch]] = s2count.get(s2[ch], 0) + 1 

        if s1count == s2count: 
            return True 
        
        for right in range(l1, l2): 
            left = right - l1 
            # Character that's entering the window is the one before left
            s2count[s2[right]] = s2count.get(s2[right], 0) + 1   
            s2count[s2[left]] -= 1 
            if s2count[s2[left]] == 0: 
                del s2count[s2[left]]

            if s1count == s2count: 
                return True 

        return False



        

        

              