class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #brute force solution, check the longest substring starting at that given index
        longest = 0
        for i in range(len(s)):
            substring = s[i] #at each index the substring starts
            longest = max(len(substring), longest)
            for j in range(i + 1, len(s)):
                if s[j] not in substring:
                    substring += s[j]
                    longest = max(len(substring), longest) #update again if we added j
                else:
                    break
        return longest
        #o(n^2) time, o(n) space worst case if the entire array is not repeating
