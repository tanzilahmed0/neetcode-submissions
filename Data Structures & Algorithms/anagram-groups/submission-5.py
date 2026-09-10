class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # It's asking for a list of lists 
        # We can use a frequency counter to see if they're anagrams
        # And then we can also have a defaultdict that stores lists of the anagrams, but 
        # I need to figure out what the key would be 
        # We can sort the strings, and then store the sorted string as the key 
        
        anagramMap = defaultdict(list)

        for s in strs: 
            sorted_s = "".join(sorted(s)) 
            anagramMap[sorted_s].append(s)

        return list(anagramMap.values())
                
        