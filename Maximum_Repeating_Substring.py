def maxRepeating(self, sequence: str, word: str) -> int:
    subsequence = word
    res = 0
    while subsequence in sequence:
        subsequence += word
        res += 1
    return res