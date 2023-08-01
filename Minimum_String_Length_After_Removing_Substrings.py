from collections import defaultdict

class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        opposite = defaultdict(int)

        opposite["A"] = "B"
        opposite["C"] = "D"

        for c in s:
            if stack and opposite[stack[-1]] == c:
                stack.pop()
            else:
                stack.append(c)
        return len(stack)