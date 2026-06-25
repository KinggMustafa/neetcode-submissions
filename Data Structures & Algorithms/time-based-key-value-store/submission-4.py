class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))
        #complexity: appending to a list o(1)
        

    def get(self, key: str, timestamp: int) -> str:
        lis = self.timemap[key] 
        l = 0
        r = len(lis)-1
        while l <= r:
            midpoint = (l+r)//2
            if lis[midpoint][0] == timestamp:
                return lis[midpoint][1]
            elif lis[midpoint][0] > timestamp:
                r = midpoint - 1
            else:
                l = midpoint + 1
        if r >= 0:
            return lis[r][1]
        return ""
        #(logn) bc we split our array in half if the answer is not found
    
            