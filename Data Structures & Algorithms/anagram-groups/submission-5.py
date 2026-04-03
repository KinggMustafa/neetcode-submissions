class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sorting is m which is the amount of strings in strs * n log n for sorting each one, so n strings in strs would result in O(n^2)
        freqtable = defaultdict(list)
        for string in strs:
            #how can we sort the chars every time in O(n)? 
            #mapping in a list
            freq = [0] * 26 #each index accounts for a letter in the alphabet
            for char in string: 
                freq[ord('a') - (ord(char))] += 1
            #the key for our dictionary will be the freq, but it must be a tuple bc python dict keys must be immutable
            freqtable[tuple(freq)].append(string)
        return list(freqtable.values())
            