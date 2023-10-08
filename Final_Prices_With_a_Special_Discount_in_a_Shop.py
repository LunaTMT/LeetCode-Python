def finalPrices(arr: list[int]) -> list[int]:
        
    stack = []
    for i, e in enumerate(arr):
        while stack and arr[stack[-1]] >= e:
            arr[stack.pop()] -= e
        stack.append(i)
    return arr
    
    

    """
    O(n^2)
    """
    
    res = []
    n = len(prices)
    for i in range(n-1):
        j = i+1
        discount = 0
        while j < n-1:
            if prices[j] <= prices[i]:
                discount = prices[j]
                break
            j += 1
        res.append(prices[i] - discount)
    return res + [prices[-1]]

finalPrices(arr = [8,4,6,2,3])