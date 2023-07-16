def interpret(self, s: str) -> str:
    res = ""
    for i in range(len(s)):
        if s[i] == "(" and s[i+1] == ")":
            res += "o"
        elif s[i].isalpha():
            res += s[i]
        else:
            pass
    return res 