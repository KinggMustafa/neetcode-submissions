class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqmap = defaultdict(int)
        left = 0 
        right = 0
        res = 0
        
        while right < len(s):
            mostfreq = 0
            freqmap[s[right]] += 1
            for count in freqmap:
                mostfreq = max(mostfreq, freqmap[count])
            if ((right - left)+1) - mostfreq <= k:
                res = max(res, (right - left)+1)
            else:
                freqmap[s[left]] -= 1
                left += 1
            right += 1
        return res
#o(n * 26) time 
#o(26) space (letters in alphabet)
                
