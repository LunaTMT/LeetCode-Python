def commonChars(self, words: List[str]) -> List[str]:
    sets = [set(word) for word in words]
    common = set.intersection(*sets)

    res = []
    for char in common:
        res += [* (char * min(word.count(char) for word in words))]
    return res

commonChars(["bella","label","roller"])