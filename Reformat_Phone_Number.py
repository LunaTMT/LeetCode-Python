def reformatNumber(self, number: str) -> str:
    number = "".join(c for c in number if c.isdigit())
    res = ""
    n = len(number) 

    if n % 3 == 0:
        res = "".join(f"{number[i:i+3]}-" for i in range(0, n, 3))
        return res[:-1]

    if n % 3 == 1:
        res = "".join(f"{number[i:i+3]}-" for i in range(0, n-4, 3))
        res += number[-4:-2] + "-" + number[-2:]
        return res

    elif n % 3 == 2:
        res = "".join(f"{number[i:i+3]}-" for i in range(0, n-2, 3))
        res += number[-2:]
        return res