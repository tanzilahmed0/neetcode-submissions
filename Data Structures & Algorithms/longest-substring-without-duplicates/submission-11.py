class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0 
        dupes = set()

        left = 0
        for i in range(len(s)):
            while s[i] in dupes: 
                dupes.remove(s[left])
                left += 1 
            dupes.add(s[i])
            length = i - left + 1         
            maxLength = max(maxLength, length)
            
            
        return maxLength
                