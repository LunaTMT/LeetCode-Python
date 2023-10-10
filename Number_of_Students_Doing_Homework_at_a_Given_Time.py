def busyStudent(self, start: List[int], end: List[int], target: int) -> int:
    return sum(s <= target <= e for s, e in zip(start, end))