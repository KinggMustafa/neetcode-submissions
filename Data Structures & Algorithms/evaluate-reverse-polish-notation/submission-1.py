class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #store each number in a stack
        stack = []
        for token in tokens: 
            if token in {'+', '-', '*', '/'}:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if token == '+':
                    stack.append(num2 + num1)
                elif token == '-':
                    stack.append(num2 - num1)
                elif token == '*':
                    stack.append(num2 * num1)
                else:
                    stack.append(num2/num1) #using the int operator makes 3.7 truncate to 0 meaning 3.7 = 3
            else:
                stack.append(token)
        return int(stack.pop())
#complexity o(n) where n is the length of tokens, and constant space bc we only get one answer


