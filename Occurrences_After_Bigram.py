from collections import defaultdict
def findOcurrences(text: str, first: str, second: str) -> list[str]:

    text = text.split()
    mapping = defaultdict(list)

    for i in range(len(text)-2):
        key = (text[i], text[i+1])
        mapping[key].append(text[i+2])

    key = (first, second)
    return mapping[key]
