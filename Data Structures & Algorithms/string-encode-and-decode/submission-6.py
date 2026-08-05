class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ''
        for string in strs:
            res += str(len(string))
            res += '-'
            res += string
        return res


    def decode(self, s: str) -> List[str]:
        curr = 0
        string = ''
        res = []
        while curr < len(s):
            if s[curr] == '-':
                length = int(string)
                string = s[curr + 1: curr + 1 + length]
                res.append(string)
                curr = curr + 1 + length
                string = ''
            else:
                string += s[curr]
                curr += 1
        return res
        #o(n) time, the most our string will operate is 200, and that pushes us up further the list 
        #constant space bc the problem wanted an output list but at most it will be the length of our original strs
        

