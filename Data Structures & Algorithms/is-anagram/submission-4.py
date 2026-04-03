class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map1 = defaultdict(int)
        map2 = defaultdict(int)

        for string in s: 
            map1[string] += 1
        
        for letter in t:
            map2[letter] += 1
        

        #check values:
        for key in map1:
            if map1[key] != map2[key]:
                return False
        return True