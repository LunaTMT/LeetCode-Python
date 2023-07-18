
def removeOuterParentheses( s: str) -> str:
    open_br = 0

    res = ""
    sub_str = ""
    for c in s:
        if c == "(":
            open_br += 1
        elif c == ")":
            open_br -= 1
        
        sub_str += c
    
        if open_br == 0:
            res += sub_str[1:][:-1]
            sub_str = ""
    return res

removeOuterParentheses("(()()) (()) ")