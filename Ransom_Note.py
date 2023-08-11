def canConstruct(self, RN: str, M: str) -> bool:
    for i in RN:
        if i in M:
            M = M.replace(i,"",1)
        else: return False
    return True
