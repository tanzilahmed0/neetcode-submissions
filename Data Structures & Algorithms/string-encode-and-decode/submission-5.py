class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs: 
            result += str(len(s)) + '#' + s

        return result
        
       

    # 4#neet4#code4#love3#you

    def decode(self, s: str) -> List[str]:
        print(s)
        result = []
        i = 0

        while i < len(s): 
            j = i
            while s[j] != '#': 
                j += 1
            length = int(s[i:j])
            result.append(s[j+1:j+length+1])
            i = j + length + 1
            
            

        return result
