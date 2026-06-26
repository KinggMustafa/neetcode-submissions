class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1freq = defaultdict(int)
        for char in s1:
            s1freq[char] += 1
        
        windowsize = len(s1)
        s2freq = defaultdict(int)
        for i in range(len(s2)):
            s2freq[s2[i]]+= 1
            if i >= windowsize:
                s2freq[s2[i-windowsize]]-=1
                if s2freq[s2[i-windowsize]] == 0:
                    del s2freq[s2[i-windowsize]]
            if s2freq == s1freq:
                return True
        return False
            
            
            



        return False
        #time complexity: o(n+m) n is the length of s1, m is the length of s2, but s1 will never be more than s2 so this approaches o(m)