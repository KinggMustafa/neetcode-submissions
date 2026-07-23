class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        start = 0
        longest = 0
        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[start])
                start += 1
            window.add(s[i])
            longest = max(longest, len(window))
        return longest