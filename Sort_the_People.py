def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
    zipped = list(zip(names, heights))
    zipped.sort(key=lambda x: x[1], reverse=True)
    names, heights = zip(*zipped)
    return names