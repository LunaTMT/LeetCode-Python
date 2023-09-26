
def reorderSpaces(self, s: str) -> str:
    spaces = s.count(' ')
    s = s.split()
    words = len(s)

    if words == 1:
        return s[0] + spaces * " "
    else:
        q, r = divmod(spaces, len(s)-1)
        return f"{q*' '}".join(word for word in s) + r * " "