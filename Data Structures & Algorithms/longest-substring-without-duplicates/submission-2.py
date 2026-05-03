class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #brute force solution, check the longest substring starting at that given index
        longest = 0
        for i in range(len(s)):
            substring = '' #at each index the substring starts
            substring += s[i]
            for j in range(i + 1, len(s)):
                if s[j] not in substring:
                    substring += s[j]
                else:
                    longest = max(len(substring), longest)
                    break
        return longest
        #o(n^2) time, o(n) space worst case if the entire array is not repeating
