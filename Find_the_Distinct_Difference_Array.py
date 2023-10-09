def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
    
    """
    Initial intuition
    """
    res = []
    pre = set()
    n = len(nums)

    for i in range(n-1):
        suf = set(nums[i+1:])
        pre.add(nums[i])
        res.append(len(pre) - len(suf))
    return res + [len(set(nums))]

    #
    
    prefix = defaultdict(int)
    suffix = Counter(nums)
    res = []
    for e in nums:
        prefix[e] += 1
        suffix[e] -= 1

        if suffix[e] == 0:
            del suffix[e]
        res.append(len(prefix) - len(suffix))
    return res

