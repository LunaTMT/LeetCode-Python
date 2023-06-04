def isPalindrome(s: str) -> bool:
    #Two pointer
    i, j = 0, len(s) - 1
    while i < j:
        a, b = s[i].lower(), s[j].lower()
        if a.isalnum() and b.isalnum():
            if a != b: return False
            else:
                i, j = i + 1, j - 1
                continue
        i, j = i + (not a.isalnum()), j - (not b.isalnum())
    return True

    #Simple 
    s = s.lower()
    s = re.sub(r'[\W_]', '', s)
    return s == s[::-1]
        
if __name__ == "__main__": 
    isPalindrome("A man, a plan, a canal: Panama")
