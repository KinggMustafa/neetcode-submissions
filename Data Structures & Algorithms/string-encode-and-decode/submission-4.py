class Solution:
    def encode(self, strs: List[str]) -> str:
        fullstring = ""
        for string in strs:
            fullstring += str(len(string)) + '*' + string
        return fullstring
    def decode(self, s: str) -> List[str]:
        length = ''
        strs = []
        i = 0
        while i < len(s): 
            if s[i] != '*':
                length += s[i]
                i += 1
            else:
                length = int(length)
                word = ''
                while length != 0:
                    word += s[i+1]
                    length -= 1
                    i += 1
                i += 1
                strs.append(word)
                length = ''
        return strs
                     
                    

                
            
        
            
        
                
            
                


            


