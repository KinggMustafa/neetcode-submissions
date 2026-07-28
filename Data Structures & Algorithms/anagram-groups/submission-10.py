class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqmap = {}
        for string in strs:
            freq = [0] * 1000
            for char in string:
                freq[ord('a') - ord(char)] += 1
            freq = tuple(freq)
            if freq in freqmap:
                freqmap[freq].append(string)
            else:
                freqmap[freq] = [string]
        return list(freqmap.values())