def areAlmostEqual(s1: str, s2: str) -> bool:
    diff = [[x, y] for x, y in zip(s1, s2) if x != y]
    return not diff or len(diff) == 2 and diff[0][::-1] == diff[1]

areAlmostEqual(s1 = "bank", s2 = "kanb")