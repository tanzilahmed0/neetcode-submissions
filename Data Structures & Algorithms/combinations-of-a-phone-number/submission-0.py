from collections import defaultdict
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
        }

        # So the order just stays the same, so we have to take any char from 3 and then pick all possible 
        # letters, so we can just recurivsely backtrack and exhaust all combinations 
        # 

        output = []
        if not digits: 
            return output
        path = []
        def backtrack(i): 
            if i == len(digits): 
                output.append("".join(path.copy()))
                return 
            for char in mapping[digits[i]]: 
                # choice to use this one or not 
                path.append(char)
                backtrack(i+1) 
                path.pop()


        backtrack(0)
        return output