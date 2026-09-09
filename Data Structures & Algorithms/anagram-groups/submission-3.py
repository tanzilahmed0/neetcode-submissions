class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list) # mapping char count to list of anagrams
        
        for s in strs: 
            char_count = [0] * 26 

            for char in s: 
                char_count[ord(char) - ord('a')] += 1 

            result[tuple(char_count)].append(s) 

        return list(result.values())

            
