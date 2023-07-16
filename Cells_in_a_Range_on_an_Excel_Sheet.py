def cellsInRange(s: str):
    s = s.split(':')

    r = (ord(s[1][0])) - (ord(s[0][0])) + 1
    c = int(s[1][1]) - int(s[0][1]) + 1

    res = []
    for row in range(r):
        print(row)
        for column in range(c):
            print(column)
            res.append(chr(ord(s[0][0]) + row) + str(int(s[0][1]) +column+1)) 

    return res

cellsInRange("A1:F1")