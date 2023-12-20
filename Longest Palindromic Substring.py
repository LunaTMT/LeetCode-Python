
def longestPalindrome(self, s: str) -> str:
    longest = 0
    res = ""
    n = len(s)

    def traverse_from_center(l, r):
        nonlocal longest, res 
        while (l >= 0 and r < n) and s[l] == s[r]:
            diff = (r - l + 1)
            if diff > longest:
                longest = diff
                res = s[l:r + 1]
            l -= 1
            r += 1

    for i in range(n):
        traverse_from_center(i, i) #Odd
        traverse_from_center(i, i + 1) #Even
    return res
