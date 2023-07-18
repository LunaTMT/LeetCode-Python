def countPoints(rings: str) -> int:
    colours = [set() for _ in range(10)]

    for i in range(1, len(rings), 2):
        colours[int(rings[i])].add(rings[i-1])
    
    return sum(True for c in colours if len(c) == 3)

countPoints("B0B6G0R6R0R6G9")