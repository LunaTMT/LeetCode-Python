def largestGoodInteger(s: str) -> str:
    return max(s[i:i+3] if s[i] == s[i+1] == s[i+2] else "" for i in range(len(s)-2))

largestGoodInteger("6777133339")