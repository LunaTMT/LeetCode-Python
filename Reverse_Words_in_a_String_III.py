import math

def reverseWords(s: str) -> str:
    #For the sake of pointer practice
    l, r = 0, 0
    s = [*s]

    while l <= len(s)-1:
        
        while s[r] != " ":
            r += 1
            
            if r > len(s)-1:
                break
        
        for i in range(math.floor((r-l)/2)):
            s[l+i], s[r-i-1] = s[r-i-1], s[l+i]

        r += 1
        l = r
    return "".join(s)

"""
First solution        
s = s.split(" ")
return " ".join(word[::-1] for word in s)"""


if __name__ == "__main__":
    reverseWords("Let's take LeetCode contest")