def repeatedNTimes(self, A: List[int]) -> int:
    # O(1)
    while 1:
        s = random.sample(A, 2)
        if s[0] == s[1]:
            return s[0]

    # O(n)  
    n = len(nums) // 2
    count = defaultdict(int)

    for e in nums:
        count[e] += 1

        if count[e] == n:
            return  e