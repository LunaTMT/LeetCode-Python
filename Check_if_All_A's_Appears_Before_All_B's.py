def checkString(self, s: str) -> bool:
    B_found = False
    for c in s:
        if c == 'b':
            B_found = True
        elif c == 'a' and B_found:
            return False
    return True 