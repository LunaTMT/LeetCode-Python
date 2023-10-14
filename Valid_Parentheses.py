def isValid(s: str) -> bool:
    d = {'(':')', '{':'}','[':']'}
    stack = []
    for i in s:
        if i in d:  # 1
            stack.append(i)
        elif len(stack) == 0 or d[stack.pop()] != i:  # 2
            return False
    return len(stack) == 0 # 3
    
    
    
    
    """opposite = {")" : "(",
                "]" : "[",
                "}" : "{"
                }
    stack = []
    for c in s:
        if stack and stack[-1] == opposite.get(c, False):
            stack.pop()
        else:
            stack.append(c)
    return stack == []"""
isValid("()")