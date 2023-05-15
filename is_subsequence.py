class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        chars = [*s]
        idx = 0
        for i in t:
            if idx == len(chars):
                return True
            elif i == chars[idx]:
                idx += 1
            else:
                pass

        return True if idx == len(chars) else False