
def subsets( nums):
    nums.sort()
    res = []

    def dfs(index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            dfs(i+1, path+[nums[i]], res)

    dfs(0, [], res)
    return res
    
subsets(nums = [1,2,3])