arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 5

l = 0
current_sum = sum(arr[0:k-1])
res = 0
for l in range(len(arr)-k):
    current_sum += arr[l+k-1]
    if current_sum/k >= threshold:
        res += 1
    
    current_sum -= arr[l]
    current_sum += arr[l+k]
print(res)
        