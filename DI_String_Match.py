def diStringMatch(self, s: str) -> List[int]:
    I, D = 0, len(s)

    numbers = []
    for i in s:
        if i == "I":
            numbers.append(I)
            I += 1
        else: 
            numbers.append(D)
            D -= 1

    return numbers + [I]