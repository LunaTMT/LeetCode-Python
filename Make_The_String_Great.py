def makeGood(self, s: str) -> str:
    stack = []
    for c in s:
        if stack and (
            c.isupper() and stack[-1] == c.lower() or 
            c.islower() and stack[-1] == c.upper()):
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)

    """ Cleaner
    stack = []
    for c in s:
        if stack and abs(ord(c) - ord(stack[-1])) == 32:
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)
    """



makeGood("leEeetcode")
