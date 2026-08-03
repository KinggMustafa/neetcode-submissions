class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left = 0
        right = 0
        res = 0
        #freq will only ever have the freq of the characters in our window
        while right < len(s):
            freq[s[right]] += 1
            maxfreq = 0
            for count in freq:
                maxfreq= max(maxfreq, freq[count])
            #we get the max freq in our window
            length = (right - left)+1
            if length - maxfreq > k:
                freq[s[left]] -= 1
                left += 1
                right += 1
            else:
                res = max(res, length)
                right += 1
        return res
            
