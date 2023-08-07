from itertools import groupby
def maxPower( s: str) -> int:
    return max( len(list(group)) for _, group in groupby(s))

maxPower("yyyzzzzzzzz")
