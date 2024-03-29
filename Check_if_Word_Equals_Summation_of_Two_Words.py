from itertools import zip_longest


def isSumEqual(w1: str, w2: str, w3: str) -> bool:

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

    """Or simply use the built in translate method on str
    table = str.maketrans('abcdefghij', '0123456789')
    return int(firstWord.translate(table)) + int(secondWord.translate(table)) == int(targetWord.translate(table))
    """

isSumEqual("aaaadaaa", "a", "aaaa")
