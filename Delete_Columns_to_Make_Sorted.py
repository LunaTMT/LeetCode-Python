def minDeletionSize(s: list[str]) -> int:
    deleted = 0
    i = 0
    while i < len(s[0]):
        column = [word[i] for word in s]
        if column != sorted(column): deleted += 1
        i += 1
    return deleted

minDeletionSize(["abc", "bce", "cae"])