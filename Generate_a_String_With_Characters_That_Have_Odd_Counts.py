def generateTheString(self, n: int) -> str:
    return n * "a" if n % 2 else (n-1) * "a" + "b"