class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        #count the frequency of each s and t, then compare the key and value pairs in the dict
        dicts = defaultdict(int) #use a default dict so that we know the value is always an integer
        dictt = defaultdict(int)
        #count the freq of each string and store it in the dict: letter: count
        for char in s:
            dicts[char] += 1
        for char in t: dictt[char] += 1
        #o(n) space and time

        for key, value in dicts.items():
            if dicts[key] != dictt[key]:
                return False
        return True

        #go through each key value pair in dicts: 
        #this solution is o(n) time, and it is actually o(1) or constant space bc: of our constraint: s and t consist of lowercase English letters.
        #the constraint means that there will ever only be 26 letters to work with a-z in both keys of the dictionary
