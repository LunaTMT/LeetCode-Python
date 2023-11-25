def combinationSum(self, arr: List[int], t: int) -> List[List[int]]:
    
    def backtrack(start, target, path):
        if target == 0:
            res.append(path)
            return
        if target < 0:
            return
        
        for i in range(start, len(arr)):
            backtrack(i, target-arr[i], path+[arr[i]])
    
    arr.sort()
    res = []
    backtrack(0, t, [])
    return res


