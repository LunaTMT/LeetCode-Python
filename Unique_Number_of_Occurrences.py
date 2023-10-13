from collections import Counter
def uniqueOccurrences(A: list[int]) -> bool:
    return (lambda x: len(x) == len(set(x)))(Counter(A).values())

    """
    OR
    """

    found = set()
    for i in Counter(arr).values():
        if i in found:
            return False
        found.add(i)
    return True

uniqueOccurrences(A = [1,2,2,1,1,3])