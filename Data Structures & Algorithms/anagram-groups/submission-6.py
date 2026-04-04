class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        worddict = defaultdict(list) #the value of our dict will be the sublist of words in strs, matching the key when they are sorted
        for word in strs:
            sorted_string = tuple(sorted(word)) #find our key to the dict. the sorted() gives back a list, "".join() would also work here   
            worddict[sorted_string].append(word)
        return list(worddict.values()) 
        #compexity: o(n * m log m) n is the length of strs, and m is the length of the word  
        