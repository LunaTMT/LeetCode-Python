from itertools import combinations
def subsetXORSum(nums: list[int]) -> int:
    res = sum(nums)
    n = len(nums)
    for i in range(2, n+1):
        for comb in combinations(nums, i):
            xor = 0
            for e in comb:
                xor ^= e
            res += xor
    return res

subsetXORSum([1,3])