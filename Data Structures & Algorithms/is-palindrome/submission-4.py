class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        def isvalid(char):
            if ord('0') <= ord(char) <= ord('9'):
                return True
            if ord('a') <= ord(char) <= ord('z'):
                return True
            return False 
        
        valid_char = ''
        for c in s:
            if isvalid(c.lower()):
                valid_char += c.lower()
        
        reversedchar = valid_char[::-1]
        if valid_char == reversedchar:
            return True
        else:
            return False

        #this is o(n) time where n is the length of the string and o(n) space where n is the length of the valid characters in the string s
        



            
