 
nums = [0, 1, 0, 1, 0]
sum_indices = {0: -1}
cur_sum = 0
max_length = 0

for i, num in enumerate(nums):
    
    cur_sum += 1 if num == 1 else -1

    if cur_sum in sum_indices:
        max_length = max(max_length, i - sum_indices[cur_sum])
    else:
        sum_indices[cur_sum] = i


