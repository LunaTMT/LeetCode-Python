def wordPattern(pattern: str, s: str) -> bool:
    L2W_hash = {}
    W2L_hash = {}

    p = pattern
    s = s.split()

    if len(p) != len(s): return False

    for letter, word in zip(p, s):
        if letter in L2W_hash and L2W_hash[letter] != word: return False
        elif word in W2L_hash and W2L_hash[word] != letter: return False
        else: 
            L2W_hash[letter] = word
            W2L_hash[word] = letter
    return True

