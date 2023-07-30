def digitCount(self, num: str) -> bool:
    count = Counter(num)
    
    for i, v in enumerate(num):
        if count[str(i)] != int(v):
            return False
    return True
