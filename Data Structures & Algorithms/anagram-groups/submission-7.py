class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #our last solution was n * m log m but if we can get rid of sorting, we can get o(n) time
        #if ord('a') = 100, then ord('c') - ('a') would be 2, which is our index in the list
        #our key in the dictionary is the list from indexing o to 25, representing each word
        worddict = defaultdict(list)
        for string in strs: 
            freqlist = [0] * 26  #bc of our constraint of only using lowercase letters
            for char in string: #length of each word m, which will 
                freqlist[ord(char) - ord('a')] += 1 
            worddict[tuple(freqlist)].append(string) #can also turn this into map(str, freq) then joining that for our dictionary key instead of using a tuple. you HAVE to join it together if you use map bc mapping does not store any values
        return list(worddict.values())
    #o(n * m) time where n is the length of strs, and m is the length of word in strs
            
            