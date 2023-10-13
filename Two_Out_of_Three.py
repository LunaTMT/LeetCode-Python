def twoOutOfThree(self, a1: List[int], a2: List[int], a3: List[int]) -> List[int]:
    count = defaultdict(int)
    for a in (set(a1), set(a2), set(a3)):
        for num in a:
            count[num] += 1
    
    return (k for k, v in count.items() if v >= 2)

    """
    or a better solutions of getting the intersection of all existing pairs in a group of 3
    (3)
    (2)
    == 3
    sets: 1, 2, 3
    pairs: (1,2), (1,3), (2,3)
    then we get the union of each intersection

    """

    a1 = set(a1)
    a2 = set(a2)
    a3 = set(a3)
    return a1 & a2 | a1 & a3 | a2 & a3