class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        freq = defaultdict(int) #freq of s
        freq2 = defaultdict(int) #freq of t
        for char in s:
            freq[char] += 1
        for char in t:
            freq2[char] += 1
        return freq == freq2
        #o(n) time and space