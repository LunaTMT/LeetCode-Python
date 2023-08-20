def findRestaurant(self, l1: List[str], l2: List[str]) -> List[str]:
    l1 = {w1 : i for i, w1 in enumerate(l1)}
    
    res = []
    least = inf
    for i2, w2 in enumerate(l2):
        if w2 in l1:
            count = l1[w2] + i2
            if count < least:
                res = [w2]
                least = count
            elif count == least:
                res.append(w2)
    return res
