class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        left = 0 
        right = 1
        res = 1
        window = set(s[left])
        while right < len(s):
            if s[right] in window:
                while s[right] in window:
                    window.remove(s[left])
                    left += 1
            window.add(s[right])
            res = max(res, len(window))
            right += 1
        return res
        #o(n) because the outer while loop runes the length of s, and the inner while loop at most will be 


        