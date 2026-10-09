class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # What if we recursively check from each character in s, and then check 
        # each word in wordDict to see if it matches the portion in s, if it does 
        # we start a new string from the next index 
        memo = {}

        def dfs(i): 
            if i in memo:
                return memo[i]

            if i == len(s): 
                return True
            
            for word in wordDict: 
                if word == s[i:i+len(word)]: 
                    if dfs(i+len(word)):
                        memo[i+len(word)] = True
                        return memo[i+len(word)]
                        
            memo[i] = False
            return memo[i]

        return dfs(0)