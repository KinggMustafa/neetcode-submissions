class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for string in strs:
            sortedstring = sorted(string)
            sortedstring = ''.join(sortedstring)
            freq[sortedstring].append(string)
        return list(freq.values())
