from collections import defaultdict

def countPairs(nums: list[int], k: int) -> int:
    cnt, d = 0, defaultdict(list)
    for i, n in enumerate(nums):
        d[n].append(i)
        
    for indices in d.values():    
        for i, a in enumerate(indices):
            for b in indices[: i]:
                if a * b % k == 0:
                    cnt += 1
    return cnt

countPairs(nums = [3,1,2,2,2,1,3], k = 2)