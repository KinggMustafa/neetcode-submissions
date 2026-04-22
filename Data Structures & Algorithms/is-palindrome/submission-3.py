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

        while left < right:
            while left < right and not isvalid((s[left]).lower()):
                left += 1

            while left < right and not isvalid(s[right].lower()):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
        #time complexity: o(n) where n is the length of s
        



            
