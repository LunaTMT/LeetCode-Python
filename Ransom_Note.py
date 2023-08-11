def canConstruct(self, RN: str, M: str) -> bool:
    return not(Counter(RN) - Counter(M))    