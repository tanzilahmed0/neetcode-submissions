class Solution:
    def isValid(self, s: str) -> bool:
        closetoopen = {')': '(', '}': '{', ']': '['}

        stack = []

        for ch in s: 
            if ch not in closetoopen.keys(): 
                stack.append(ch)
            else:
                if stack and closetoopen[ch] == stack[-1]: 
                    stack.pop()
                else: 
                    return False
        return not stack
        