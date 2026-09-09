class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): 
            return False

        hashS = {}
        hashT = {} 

        for i in s: 
            hashS[i] = hashS.get(i, 0) + 1

        for i in t: 
            hashT[i] = hashT.get(i, 0) + 1

        if hashS == hashT: 
            return True 
        else: 
            return False
        
        