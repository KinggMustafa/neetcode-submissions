class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = defaultdict(int)
        for s in s1:
            freq1[s]+= 1
        
        
        right = len(s1) -1
        for i in range(0, len(s2) - len(s1)+ 1):
            window = defaultdict(int)
            for j in range(i, (i + right) + 1):
                window[s2[j]] += 1
            if window == freq1:
                return True
        return False


