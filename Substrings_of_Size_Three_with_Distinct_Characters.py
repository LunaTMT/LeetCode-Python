class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0

        i = 0
        while i < len(s)-2:
            substring = s[i] + s[i+1] + s[i+2]
            if len(set(substring)) == len(substring):
                res += 1
            i += 1
        return res
        