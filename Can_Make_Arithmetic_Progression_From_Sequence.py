def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
    arr.sort()
    step = abs(arr[0] - arr[1])

    for i in range(2, len(arr)):
        diff = abs(arr[i-1] - arr[i])
        if diff != step:
            return False
    return True

"""
OR we can use the method without sorting

    n = len(arr)
    min_ = min(arr)
    max_ = max(arr)

    numbers = set(arr)
    diff = (max_ - min_)/(n-1)
    
    for i in range(n):
        expected = min_ + i * diff
        if expected not in numbers:
            return False
    return True
    
we can work out the step of an arithmetic sequence using (diff equation)

and just check every value in the range from (min_) i.e begining term in the sequence is found within the set

"""