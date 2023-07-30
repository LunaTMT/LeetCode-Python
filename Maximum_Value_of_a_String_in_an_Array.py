def maximumValue(self, strs: List[str]) -> int:
    lens = [int(s) if s.isdigit() else len(s) for s in strs]
    return 0 if not lens else max(lens)