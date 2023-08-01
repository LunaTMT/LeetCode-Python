def numberOfLines(self, widths: List[int], s: str) -> List[int]:
    lines, line = 1, 0
    for c in s:
        value = widths[ord(c) - 97]
        line += value
        if line > 100:
            lines += 1
            line = value
    return lines, line