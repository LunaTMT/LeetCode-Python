def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    banned = set(banned)
    
    punctuation = set('''!()-[]{};:'"\,<>./?@#$%^&*_~''')
    string = "".join(c.lower() if c not in punctuation else " " for c in paragraph)
    
    count = Counter(string.split())
    for tup in count.most_common():
        if tup[0] not in banned:
            return tup[0]