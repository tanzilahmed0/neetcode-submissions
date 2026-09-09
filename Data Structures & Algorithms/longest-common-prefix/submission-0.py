class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = ''

        # Use first string as a reference to compare to all the other strings
        for i in range(len(strs[0])): 
            # Check every string in strs
            for s in strs:
                # if the current index is out of bounds or they don't match return 
                # Only after we confirm we don't return do we add to prefix
                if i == len(s) or s[i] != strs[0][i]:
                    return prefix 
            prefix += strs[0][i]
        
        return prefix
        