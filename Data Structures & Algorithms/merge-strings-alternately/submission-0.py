class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left, right = 0, 0 

        result = ""

        while left < len(word1) and right < len(word2):
            result += word1[left] 
            result += word2[right] 
            left += 1 
            right += 1 
        
        if left < len(word1):
            result += word1[left:] 
        elif right < len(word2): 
            result += word2[right:]

        return result