class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1freq = defaultdict(int)
        for s in s1:
            s1freq[s] += 1
        
        #count the freq of s1

        #our window size is determined by s1
        for i in range((len(s2) -len(s1)) + 1):
            windowfreq = defaultdict(int)
            right = len(s1)-1 + i #how big the window must be at each index
            left = i
            while left <= right and right < len(s2):
                windowfreq[s2[left]] += 1
                left += 1
            if windowfreq == s1freq:
                return True
        return False    
        #complexity: o(n - m) times m where n is the length of s2, and m is the length of s1