import collections
from bisect import bisect

class TimeMap:
    def __init__(self):
        self.meta = collections.defaultdict(list)
        self.data = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.meta[key].append(timestamp)
        self.data[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect(self.meta[key], timestamp)
        if idx == 0:
            return ''
        return self.data[key][idx - 1]


timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
timeMap.get("foo", 1)        
timeMap.get("foo", 3)        
timeMap.set("foo", "bar2", 3)
timeMap.set("foo", "bar2", 4)
timeMap.set("foo", "bar2", 6)
      
timeMap.get("foo", 7)      