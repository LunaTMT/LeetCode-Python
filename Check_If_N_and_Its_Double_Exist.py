def checkIfExist(arr: list[int]) -> bool:
    arr.sort()
    l = 0
    r = 1

    
    for i, left in enumerate(arr):
        for right in arr[i+1:]:
            
            half = left/2
            double = 2*left
            
            if right in (half, double):
                return True
            elif left < 0 and (right > half):
                break 
            elif left > 0 and (right > double):
                break
            r += 1
        l += 1
        r = l+1
    return False

checkIfExist([-16,-13,8])