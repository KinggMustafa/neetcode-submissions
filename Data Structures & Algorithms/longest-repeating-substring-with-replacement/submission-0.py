class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqmap = defaultdict(int)
        
        left = 0
        longest = 0
        for right in range(len(s)):
            freqmap[s[right]] += 1
            while right - left + 1 - max(freqmap.values()) > k:
                freqmap[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)
        return longest





                


