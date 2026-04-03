class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         #26 letters in the alphabet..
        freq = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string: 
                count[ord(char) - ord('a')] += 1
            #thats our freq
            #so our key will be that but keys cannot be mutable such as lists, we cannot loop through keys..
            freq[tuple(count)].append(string)
        return list(freq.values())
