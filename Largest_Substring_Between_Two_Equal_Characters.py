def maxLengthBetweenEqualCharacters(s: str) -> int:
    res, positions = -1, {}

    for i, c in enumerate(s):
        res = max(res, i - positions.setdefault(c, i + 1))
    return res

maxLengthBetweenEqualCharacters('BACABBBA')