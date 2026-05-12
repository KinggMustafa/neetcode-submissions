class MinStack:

    def __init__(self):
        self.stack = []
        self.minimumstack = [] 
        #initialize two stacks, that will always be the same height
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimumstack:
            self.minimumstack.append(min(val, self.minimumstack[-1]))
        else:
            self.minimumstack.append(val)
        #the minimum correspons to each index of the stack 

    def pop(self) -> None:
        self.stack.pop()
        self.minimumstack.pop()
        #remove both the element at the top of the stack, and the running minimum at that index
        

    def top(self) -> int:
        return self.stack[-1]

        

    def getMin(self) -> int:
        return self.minimumstack[-1]
    #all operations are o(1)
