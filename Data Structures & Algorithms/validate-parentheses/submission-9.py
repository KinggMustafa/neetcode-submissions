class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        lastopen = [] #[,(,
        for char in s:
            if char in pairs:
                if lastopen:
                    opener = lastopen.pop()
                    if opener != pairs[char]:
                        return False
                else:
                    return False
            else:
                lastopen.append(char)
        if not lastopen:
            return True
        else:
            return False
        #o(n) time where n is the length of s, and our space is constant bc its a fixed amount of key, value pairs