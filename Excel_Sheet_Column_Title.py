import string

def convertToTitle(self, n: int) -> str:
    alphabet = list("Z" + string.ascii_uppercase)
    res = ""
    while n:
        n, r = divmod(n, 26)
        res = alphabet[r] + res
        if not r: n -= 1
    return res

convertToTitle(702)