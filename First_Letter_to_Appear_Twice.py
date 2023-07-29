def repeatedCharacter(self, s: str) -> str:
    letters = set()
    for c in s:
        if c not in letters:
            letters.add(c)
        else: 
            return c