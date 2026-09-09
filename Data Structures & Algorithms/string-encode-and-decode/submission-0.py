class Solution:

    def encode(self, strs: List[str]) -> str:
        # Empty list to store the strings
        check = []

        # Want to store the length of the strings, so have it as fixed
        # digit of length 4
        # then add to empty list with '@' delimiter between length and 
        # original string
        for s in strs: 
            modified_string = str(len(s)).zfill(4)
            check.append(modified_string + '@' + s)
        
        # then join the strings together with '~' delimiter
        check = "".join(check)

        return check 
             

    def decode(self, s: str) -> List[str]:
        if not s: 
            return []

        result = [] 
        i = 0

        while i < len(s): 
            print(f"Index i: {i}. Slice to read: '{s[i:i+4]}'")
            length = int(s[i:i+4])
            i = i + 5
            # 0004@neet~0004@code~0004@love
            original_word = s[i:i+length]
            result.append(original_word)
            i = i + length

    
        return result
