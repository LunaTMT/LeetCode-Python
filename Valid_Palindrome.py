def isPalindrome(s: str) -> bool:
    s = "".join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

    """
    O(1) space (two-pointer)
    """

    i, j = 0, len(s)-1

    while i < j:
        a, b = s[i].lower(), s[j].lower()
        if a.isalnum() and b.isalnum():
            if a != b: return False
            else:
                i += 1
                j -= 1
        i += not a.isalnum()
        j -= not b.isalnum() 
    return True