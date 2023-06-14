def minimumDifference(nums: list[int], k: int) -> int:
	if len(nums) <= 1:
		return 0

	nums = sorted(nums)
	res = nums[k-1] - nums[0]

	for i in range(k, len(nums)):
		res = min(res, nums[i] - nums[i - k + 1])

	return res

if __name__ == "__main__":
	minimumDifference( [9,4, 12, 15, 5, 2, 9, 1,7], 3)