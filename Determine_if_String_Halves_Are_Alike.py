def halvesAreAlike(s: str) -> bool:
    mid = int(len(s)/2)
    vowels = set(('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'))
        
    s1 = s[:mid]
    s2 = s[mid:]

    s1_count = s2_count = 0
    for v1, v2 in zip(s1, s2):
        if v1 in vowels: 
            s1_count += 1
        if v2 in vowels:
            s2_count += 1

    return s1_count == s2_count

halvesAreAlike("textbook")
