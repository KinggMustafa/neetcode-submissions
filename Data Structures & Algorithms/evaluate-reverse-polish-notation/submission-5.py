class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #build a stack of numbers, and use 2 per operation
        stack = []
        for num in tokens: 
            if num in {'+', '-','*','/'}:
                num1 = stack.pop()
                num2 = stack.pop()
                if num == '+':
                    stack.append(num2+num1)
                elif num == '-':
                    stack.append(num2-num1)
                elif num == '*':
                    stack.append(num2*num1)
                else:
                    stack.append(int(num2/num1)) #we do int to make it truncate toward 0, 3.7 turns into 3
            else:
                stack.append(int(num))
        return stack.pop()
                