def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    count = [0]*101

    for num in nums:
        count[num] += 1

    return (sum(count[:num]) for num in nums)
