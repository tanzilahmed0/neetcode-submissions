from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        CounterS = Counter(s)
        CounterT = Counter(t)

        return CounterS == CounterT