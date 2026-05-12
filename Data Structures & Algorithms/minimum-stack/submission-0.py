class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        val = float('INF')
        for value in self.stack:
            if value < val:
                val = value
        return val
        #this is o(n) but we want every operation to be o(1)
        
