def isLongPressedName(name: str, typed: str) -> bool:
    i = j = 0
    while i < len(typed) and j < len(name):
        if typed[i] == name[j]:
            i += 1
            j += 1
        else:
            if typed[i] == typed[i-1] and i != 0:
                i += 1
            else: 
                return False
    if set(typed[i-1:]) != set(name[j-1:]):
        return False
    else: return True

"""
OR

    nL = len(name)
    tL = len(typed)
    i = j = 0
    while i <= nL and j < tL:
        if i < nL and typed[j] == name[i]:
            j += 1
            i += 1
        elif typed[j] == name[i-1] and i != 0:
            j += 1
        else:
            return False
    return i == nL and j == tL
"""


name = "bdad"
typed = "bbbd"

isLongPressedName(name, typed)