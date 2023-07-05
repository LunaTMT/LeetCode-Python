def isStrictlyPalindromic(self, n: int) -> bool:
    def is_new_base_palindromic(n, b):
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
        return digits == digits[::-1]

    for i in range(2, n-1):
        if not is_new_base_palindromic(n, i): return False
    return True

    #OR JUST RETURN FALSE??!?!?!?!