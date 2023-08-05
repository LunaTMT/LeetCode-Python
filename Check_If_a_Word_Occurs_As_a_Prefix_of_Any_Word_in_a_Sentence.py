def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:   
    for i, word in enumerate(sentence.split(' '), start=1):
        if word[:len(searchWord)] == searchWord:
            return i
    return -1