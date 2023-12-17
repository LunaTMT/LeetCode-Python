def permute(self, nums: List[int]) -> List[List[int]]:
    
    visited = set()
    res = []

    def backtrack(path, visited):

        if len(path) == len(nums):
            res.append(path.copy())
            return

        for i in nums:
            if i not in visited:
                visited.add(i)
                backtrack(path + [i], visited)
                visited.remove(i)  
    
    backtrack([], visited)
    return res
