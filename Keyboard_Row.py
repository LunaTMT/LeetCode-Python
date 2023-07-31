def findWords(words: list[str]) -> list[str]:
    r1 = set("qwertyuiop")
    r2 = set("asdfghjkl")
    r3 = set("zxcvbnm")
    
    def check_valid(word):
        for r in (r1, r2, r3):
            valid = True
            for c in word:
                if c.lower() not in r:
                    valid = False
                    break
            if valid:
                return word
        return None

    valid = map(check_valid, words)
    return [i for i in valid if i is not None]