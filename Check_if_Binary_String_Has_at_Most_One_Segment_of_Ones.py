def checkOnesSegment(self, s: str) -> bool:
    return '01' not in s

    """
    zero = False

    for c in s:
        if c == "0" and not zero:
            zero = True
        
        elif zero and c == "1":
            return False
    return True
    """