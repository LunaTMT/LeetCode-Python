def removeTrailingZeros(self, num: str) -> str:
    for i, n in enumerate(reversed(num)):
        if n != "0":
            return num[:len(num)-i]

    #Or simply!
    return num.rstrip('0')
