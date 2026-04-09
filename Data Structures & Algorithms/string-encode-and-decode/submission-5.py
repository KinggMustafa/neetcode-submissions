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
                word = s[i + 1: i + length + 1] #start: end , includes start, excludes end
                strs.append(word)
                i += (length + 1) #start the index after the final letter of the string
                length = ''
        return strs
    #(o(n) time and o(n) space where n is the total number of characters from all strings, and o(n) space and time for decode where n is the length of the string
                     
                    

                
            
        
            
        
                
            
                


            


