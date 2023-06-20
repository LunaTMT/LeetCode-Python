class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l, r = 0, len(s)-1
        s = [*s]

        while l < r:
            if s[l] == s[r]:
                pass
            elif s[l] < s[r]:
                s[r] = s[l] 
            else: 
                s[l] = s[r] 
           
            l += 1
            r -= 1
        return "".join(s)