class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        unicode = [0] * 26
        for i in range(len(s)):
            unicode[ord('a') - ord(s[i])] += 1
            unicode[ord('a') - ord(t[i])] -= 1
        for code in unicode:
            if code:
                return False
        return True
        #O(n) time but this beats the space complexity of our last algo