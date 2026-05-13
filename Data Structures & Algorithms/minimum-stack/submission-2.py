class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = [] #keep a running min, at each index there is a running min


    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            currmin = self.minstack[-1]
            self.minstack.append(min(currmin, val))
        else:
            self.minstack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop() #get rid of the curr min at that given index too 
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        #instead of doing a for loop, to keep this o(1) per operation we can have a min stack at each given index
        return self.minstack[-1]