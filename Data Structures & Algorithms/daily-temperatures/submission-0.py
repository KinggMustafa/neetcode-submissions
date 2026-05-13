class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * (len(temperatures)-1)
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    output[i] = j-i
                    break
        output.append(0)
        return output
#brute force solution o(n^2) time and o(n) space, where n is the len of temperatures
        

