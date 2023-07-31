def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
    words = [word.split(separator) for word in words]
    return [word for arr in words for word in arr if word]