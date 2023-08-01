def countCharacters(self, words: List[str], chars: str) -> int:

    res = 0
    for word in words:
        valid = True
        for c in word:
            if word.count(c) > chars.count(c):
                valid = False
                break
        if valid:
            res += len(word)
    return res