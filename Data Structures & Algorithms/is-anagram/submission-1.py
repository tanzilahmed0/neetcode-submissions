class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS, hashT = {}, {} 

        if len(s) != len(t): 
            return False 


        # Get method returns the hash maps current count at that key 
        # If it's 0, it returns 0 as default value and increments it by 1
        for i in s: 
            hashS[i] = hashS.get(i, 0) + 1

        for j in t:
            hashT[j] = hashT.get(j, 0) + 1

        for i in hashS: 
            if hashS[i] != hashT.get(i, 0): 
                return False 
            
        return True

        
        