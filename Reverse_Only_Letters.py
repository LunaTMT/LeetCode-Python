def reverseOnlyLetters(s: str) -> str:
    s = s.split(" ")
    print(s)
    l, r = 0, len(s)-1 
    

    while l < r:
        if not s[l].isalpha():
            l += 1
        elif not s[r].isalpha():
            r -= 1
        else:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
    return s

if __name__ == "__main__":
    reverseOnlyLetters("ab-cd")