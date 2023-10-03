def largestAltitude(self, gain: List[int]) -> int:
    max_ = 0
    current = 0
    for g in gain:
        current += g
        max_ = max(max_, current)
    return max_