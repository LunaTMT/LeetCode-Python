def thousandSeparator(n: int) -> str:

    s = [*str(n)]
    n = len(s)
    ans = ''
    for i in range(n):
        ans += s[i]
        if (i != n-1) and (( n - ( i + 1)) % 3 == 0):
            ans+='.'
    return ans
    
    """
    OR
    
    s = str(n)
    s = s[::-1]
    s = ".".join(s[i:i+3] for i in range(0, len(s), 3))
    return s[::-1]

    """

thousandSeparator(n =123456)