class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        substring = set()
        longest = 0
        for char in s:
            while char in substring: 
                substring.remove(s[left])
                left += 1
            substring.add(char)
            longest = max(longest, len(substring))
        return longest
        #complexity: 
        #space ~ o(n), -> worst case if the whole string is unique
        #time ~ o(n), where n is the length of s, and the while loop does not make it o(n^2) because it will never go past the right pointer



