def backspaceCompare(self, s: str, t: str) -> bool:
    s_stack = []
    t_stack = []
    
    for i in s:
        if i == "#":
            if s_stack: s_stack.pop()
        else:
            s_stack.append(i)
    
    for j in t:
        if j == "#":
            if t_stack:
                t_stack.pop()
        else:
            t_stack.append(j)

    return s_stack == t_stack

    def backspace(acc, e):
        if e != '#': acc.append(e)
        elif acc: acc.pop()
        return acc
        return reduce(back, S, []) == reduce(back, T, [])
    return reduce(back, S, []) == reduce(back, T, [])