def captureForts(forts: list[int]) -> int:

    opposites = { 1: -1,
                -1: 1}
    current = None
    i = 0
    count = 0
    res = 0
    start = False
    while i < len(forts):
        if (current := forts[i]) in opposites:
            
            if start and (current != starting_value):
                res = max(res, count)
            else:
                start = True

            starting_value = forts[i]
            count = 0
        else:
            count += 1
        i += 1
    return res

captureForts([0,-1,-1,0,-1])