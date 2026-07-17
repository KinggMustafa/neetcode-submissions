class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([value,timestamp])
        #(constant time o(1))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        sublists = self.timemap[key]
        l = 0
        r = len(sublists)-1
        while l <= r:
            mid = (l + r)//2
            if sublists[mid][1] > timestamp:
                r = mid - 1
            else:
                res = sublists[mid][0]
                l = mid + 1
        return res
        #O(logn) time 

