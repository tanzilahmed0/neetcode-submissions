from collections import Counter 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sCount, tCount = Counter(s), Counter(t)
        return sCount == tCount

        