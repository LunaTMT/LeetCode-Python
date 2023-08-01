def toGoatLatin(self, s: str) -> str:
    s = s.split(" ")
    vowels = set("aeiouAEIOU")

    for i, word in enumerate(s):
        if word[0] in vowels:
            s[i] += "ma"
        else:
            s[i] = s[i][1:] + s[i][0] + "ma"
        s[i] += (i + 1) * "a"
    
    return " ".join(s)