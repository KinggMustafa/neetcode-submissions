class Solution:

    def encode(self, strs: List[str]) -> str:
        #encode using ord operation
        newword = ""
        for string in strs:
            newword += string + "-"
        return newword

    def decode(self, s: str) -> List[str]:
        #decode using ord operation and backtracking
        new_list = []
        currword = ""
        for char in s:
            if char != "-":
                currword += char
            else:
                new_list.append(currword)
                currword = ""
        return new_list



