nums = [3,2,2,3]

count = 0
val = 3

for v in nums:
    if v != val:
        nums[count] = v
        count += 1

print(count)