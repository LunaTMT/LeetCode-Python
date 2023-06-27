class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = len(arr1)
        for a in arr1:
            for i, b in enumerate(arr2):
                if abs(a - b) <= d:
                    count -= 1
                    break
        return count