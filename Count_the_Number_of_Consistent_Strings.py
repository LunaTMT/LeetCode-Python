def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

    allowed = set(allowed)
    count = 0
    for word in words:
        for char in set(word):
            if char not in allowed:
                count += 1
                break

    return len(words) - count