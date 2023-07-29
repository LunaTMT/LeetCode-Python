from itertools import zip_longest


def isSumEqual(w1: str, w2: str, w3: str) -> bool:
    # w1 = (ord(c) - ord('a') for c in w1 if c != a)
    
    res = ["", "", ""]

    for i, word in enumerate((w1, w2, w3)):
        other_found = False
        for c in word:
            if c != 'a': 
                res[i] += str(ord(c) - ord('a'))
                other_found = True
            elif other_found:
                res[i] += str(ord(c) - ord('a'))

    res = [int(str_) if str_ else 0 for str_ in res]

isSumEqual("aaaadaaa", "a", "aaaa")