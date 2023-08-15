def maxScore(s: str) -> int:
    L = 0
    R = s.count("1")
    res = 0
    for i in range(len(s)-2):
        if s[i] == 0:
            L += 1
        else:
            R -= 1
        res = max(res, L+R)
    return res

    """ OR
        def maxScore(self, s: str) -> int:
        score = max_ = s[1:].count('1')+(1 if s[0]=='0' else 0)
        for i in range(1, len(s)-1):
            score += 1 if s[i]=='0' else -1
            max_ = max(score, max_)
        return max_
    """

maxScore("00")
