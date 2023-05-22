
from collections import defaultdict
import heapq
from operator import itemgetter


def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    
    f = k
    count = defaultdict(int)

    for i in nums:
        count[i] += 1
    heap = heapq.nlargest(k, count.items(), key=itemgetter(1)) 
    return [i[0] for i in heap]
        