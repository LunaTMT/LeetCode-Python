from collections import Counter
def numberOfPairs(nums: list[int]) -> list[int]:

    pairs = sum(cnt // 2 for cnt in Counter(nums).values())
    print()

    #Or
    seen = set()
    pairs = 0
    for i in nums:
        if i in seen:
            seen.remove(i)
            pairs += 1
        else:
            seen.add(i)
    return (pairs, len(seen))

numberOfPairs(nums = [1,3,2,1,3,2,2])