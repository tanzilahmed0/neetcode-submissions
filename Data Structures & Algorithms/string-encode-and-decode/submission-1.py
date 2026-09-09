class Solution:

    def encode(self, strs: List[str]) -> str:

        result=''
        
        for s in strs: 
            result += str(len(s)) + '@' + s 
               
        return result


        # can use @ as delemiter, and store length of string at start 
        # 4@neet~5@code~4@love~3@you
        


    def decode(self, s: str) -> List[str]:
        result = [] 
        i = 0
        new_string = ''

        while i < len(s): 
            j = i 
            while s[j] != '@': 
                j += 1
            length = int(s[i:j])
            i += j
        
            result.append(s[j+1:j+length+1])
            i = j + 1 + length

        
        return result


