class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1freq = defaultdict(int)
        for char in s1:
            s1freq[char] += 1
        
        windowsize = len(s1)
        for i in range((len(s2)-len(s1))+1):
            s2freq = defaultdict(int)
            window = s2[i:i + windowsize]
            for char in window:
                s2freq[char] += 1
            if s2freq == s1freq:
                return True
        return False
        #time complexity: o(n*m) n is the length of s1, m is the length of s2
