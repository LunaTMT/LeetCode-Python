from typing import List
def dailyTemperatures(T: List[int]) -> List[int]:
    ans = [0] * len(T)
    stack = []

    for i, e in enumerate(T):
        while stack and stack[-1][1] < e:
            index, element = stack.pop()
            ans[index] = i - index
        stack.append([i, e])
    return ans


dailyTemperatures(T = [73,74,75,71,69,72,76,73])
#Input:  [73,74,75,71,69,72,76,73]
#Output: [ 1, 1, 4, 2, 1, 1, 0, 0]