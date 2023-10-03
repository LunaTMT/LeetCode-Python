def isAcronym(self, words: list[str], s: str) -> bool:
    n = len(s)
    if len(words) != n:
        return False

    for i in range(n):
            if s[i] != words[i][0]:
                return False
    return True

def isAcronym(self, words: List[str], s: str) -> bool:
        return ''.join(word[0] for word in words) == s