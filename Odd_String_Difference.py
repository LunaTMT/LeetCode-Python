def oddString(self, words: List[str]) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    indexes = {k:v for v, k in enumerate(alphabet)}

    diff = [[indexes[word[i]] - indexes[word[i-1]] for i in range(1, len(word))] for word in words]

    for i in range(len(diff)):
        if diff.count(diff[i]) == 1:
            return words[i]
