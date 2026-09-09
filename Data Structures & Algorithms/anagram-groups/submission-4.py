from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Two words being an anagram means that if they're sorted, they're identitcal. 
        # Thus we can make a defaultdict where each key is the sorted word, and the values are the original words

        anagrams = defaultdict(list)
        for s in strs: 
            key = "".join(sorted(s)) 
            anagrams[key].append(s)

        return list(anagrams.values())
        
            