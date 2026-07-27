class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for string in strs:
            freq = defaultdict(int)
            for char in string:
                freq[char] += 1
            key = tuple(sorted(freq.items()))
            if key in table:
                table[key].append(string)
            else:
                table[key] = [string]
        return list(table.values())
            