class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for string in strs:
            freq = [0] * 26
            for char in string:
                freq[ord('a') - ord(char)] += 1
            key = tuple(freq)
            if key in table:
                table[key].append(string)
            else:
                table[key] = [string]
        return list(table.values())
            