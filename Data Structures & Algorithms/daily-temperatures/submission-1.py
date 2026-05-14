class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #[]
        output = [0] * len(temperatures) #[0,0,0,0,0,0]
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                lasttemp = stack.pop()
                output[lasttemp] = i - lasttemp
            stack.append(i)
        return output
        #o(n) where n is the length of temperatures, o(n) space, worst case we store all of our indexs