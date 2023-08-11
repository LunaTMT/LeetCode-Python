def slowestKey(self, times: list[int], keys: str) -> str:
    largest = times[0]
    res = [keys[0]]

    for i in range(1, len(times)):
        diff = (times[i] - times[i-1])

        if diff > largest:
            largest = diff
            res = [keys[i]]
        elif diff == largest:
            res += keys[i]
    
    res.sort()
    return res[-1]

slowestKey([12,23,36,46,62], ("spuda"))