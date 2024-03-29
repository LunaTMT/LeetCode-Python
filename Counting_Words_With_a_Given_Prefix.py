def prefixCount(self, words: List[str], pref: str) -> int:
    count = 0
    for word in words:
        if word[:len(pref)] == pref:
            count += 1
    return count

    #or
    return sum(word.startswith(pref) for word in words)
