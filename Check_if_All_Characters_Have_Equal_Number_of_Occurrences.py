def areOccurrencesEqual(s: str) -> bool:
    count = {}
    for c in s:
        if c not in count:
            count[c] = 1
        else:
            count[c] += 1
    return len(set(count.values())) == 1

    # or can simply use counter
    # return len(set(Counter(s).values())) == 1

areOccurrencesEqual("abacbc")
