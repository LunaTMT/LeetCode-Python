def capitalizeTitle(self, s: str) -> str:
    return " ".join(word.title() if len(word) > 2 else word.lower() for word in s.split())