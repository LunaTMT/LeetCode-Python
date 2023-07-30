def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
    text = text.split(' ')

    res = 0
    for word in text:
        valid = True
        for c in word:
            if c in brokenLetters:
                valid = False
                break
        if valid: res += 1
    return res