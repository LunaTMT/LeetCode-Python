def lengthOfLongestSubstring(s: str) -> int:
    """
    
    SLIDING WINDOW
    """
    
    seen = {}
    l = 0
    output = 0
    for r in range(len(s)):

        if s[r] not in seen:
            output = max(output,r-l+1)

        else:
            if seen[s[r]] < l:
                output = max(output,r-l+1)
            else:
                l = seen[s[r]] + 1
        seen[s[r]] = r
    return output



"""
SLOW

    res = 0
    if len(s) == 1: return 1

    for i, c in enumerate(s):
        count = {c : 1}
        for j in range(i+1, len(s)):
            if s[j] not in count:
                count[s[j]] = 1
            else:
                break
        res = max(res, sum(count.values()))
    
    return res
"""


lengthOfLongestSubstring("abcabcbb")