
def removeOuterParentheses( s: str) -> str:
    open_br = 0
    res = ""
    sub_str = ""
    for c in s:
        open_br += 1 if c == "(": else - 1
        sub_str += c
    
        if open_br == 0:
            res += sub_str[1:][:-1]
            sub_str = ""
    return res


    """
    OR
    open_br = 0
    res = []
    
    for c in s:
        if c == "(" and open_br > 0: res.append(c)
        if c == ")" and open_br > 1: res.append(c)
        open_br += 1 if c == "(" else - 1

    return "".join(res)
    """

removeOuterParentheses("(()()) (()) ")
