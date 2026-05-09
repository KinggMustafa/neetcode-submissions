class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        lastopen = []
        for key in s:
            if key in pairs.keys() and lastopen:
                val = lastopen.pop()
                if pairs[key] != val:
                    return False
            else:
                lastopen.append(key)
        if lastopen:
            return False
        return True
        #o(n) time where n i the length of s. constant space bc we only have 3 key,val pairs