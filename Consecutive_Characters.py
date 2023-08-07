def maxPower(self, s: str) -> int:
    count = res = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
            if count > res:
                res = count
        else:
            count = 1
    return res


maxPower("yyyzzzzzzzz")