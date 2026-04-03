class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #edge case: if the strings are equal but not the same length

        dictionaryofdicts = defaultdict(list)
        
        for i in range(len(strs)):
            #create dictionary of values, compare with existing sublists
            map1 = defaultdict(int)
            for char in strs[i]:
                map1[char] += 1
            #this creates a dictionary of letters, and their frequency's
            #all we need to do now is: find a key that will group the anagrams together and the value of that dictionary will be the strings 
            #our problem here is that you cant use a dictionary as a key because keys must be unchangeable (immutable)
            key = tuple(sorted(map1.items())) 
            dictionaryofdicts[key].append(strs[i])
        return list(dictionaryofdicts.values())

