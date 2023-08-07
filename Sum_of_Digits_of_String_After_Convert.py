def getLucky(s: str, k: int) -> int:
    s = "".join(str(ord(c) - 96) for c in s)
    
    for _ in range(k):
        s = str(sum(int(digit) for number in s for digit in number))
    return int(s)
    
getLucky("iiii", 2)