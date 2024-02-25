class Solution():
    def pathSum(self, root, target):
        # define global result and path
        self.result = 0
        cache = {0:1}
        
        # recursive to get result
        self.dfs(root, target, 0, cache)
        
        # return result
        return self.result
    
    def dfs(self, root, target, currPathSum, cache):
        # exit condition
        if root is None:
            return  
        
        # calculate currPathSum and required oldPathSum
        currPathSum += root.value
        oldPathSum = currPathSum - target
        
        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        
        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one. 
        cache[currPathSum] -= 1


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def array_to_tree(nums, index=0):
    if index < len(nums):
        value = nums[index]
        if value is None:
            return None
        node = TreeNode(value)
        node.left = array_to_tree(nums, 2 * index + 1)
        node.right = array_to_tree(nums, 2 * index + 2)
        return node
    return None

# Given array
array = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]

# Convert array to tree
root = array_to_tree(array)


s = Solution()
s.pathSum(root, 8)