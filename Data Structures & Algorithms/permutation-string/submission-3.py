class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = [0] * 26
        for s in s1:
            freq1[ord(s) - ord('a')]+= 1
        
        window = [0] * 26
        left = 0
        for i in range(len(s2)):
            window[(ord(s2[i]) - ord('a'))] += 1
            if i - left + 1 > len(s1):
                window[ord(s2[left]) - ord('a')] -= 1
                left += 1
            if window == freq1:
                return True
        return False
        #o(n) time and constant space bc our array will always be 26 size

            

