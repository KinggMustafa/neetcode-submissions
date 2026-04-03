class Solution:
    def encode(self, strs: List[str]) -> str:
            #they way we are going to encode the string is by using the length and then using a special character 
        newstring = ""
        for string in strs: 
            length = len(string)
            newstring += str(length) + '&' + string
        return newstring
            
        #4&hello
    def decode(self, s: str) -> List[str]:
            #for each char, once we see the length followed by our character, we know that we have a string next
        i = 0
        j = 0
        new_list = []
        while i < len(s) and j < len(s):
            if s[j] == '&':
                length = int(s[i:j]) #the length of our word would be i to j
                new_list.append(s[j +1  : (j + 1) + length])
                i = (j + 1) + length 
                j = i
            else:
                j += 1
        return new_list
                    


                
            
                


            


