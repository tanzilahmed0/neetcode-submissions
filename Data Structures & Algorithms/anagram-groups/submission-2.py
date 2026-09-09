class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list) # mapping char count to list of anagrams
        
        for s in strs: 
            char_count = {} 

            for char in s: 
                char_count[char] = char_count.get(char, 0) + 1
            
        
        # Then you have to get tuple key 
        # Sorted it to get correct order
            keys = tuple(sorted(char_count.items()))

            
            result[keys].append(s)

            
        
        return list(result.values())
