class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([value, timestamp])
        #o(1) time        

    def get(self, key: str, timestamp: int) -> str:
        sublists = self.timemap[key]

        l = 0
        r = len(sublists)-1
        res = ""
        while l <= r:
            mid = (l + r)//2
            if sublists[mid][1] <= timestamp:
                res = sublists[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
        #o(logn) time where n is the number of sublists in sublists
    
