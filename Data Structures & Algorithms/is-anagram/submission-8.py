class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #count the freq of each
        if len(s) != len(t): 
            return False #n time
        hashmap1 = defaultdict(int) 
        hashmap2 = defaultdict(int)
        for char in s: 
            hashmap1[char] += 1 #n space
        for char in t: 
            hashmap2[char] += 1 #n space

        for key, value in hashmap1.items():
            if value != hashmap2[key]:
                return False
        return True 
        # this solution is o(n) space, but o(n) time which is better than sorting. 
