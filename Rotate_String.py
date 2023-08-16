def rotateString(s: str, g: str) -> bool:
    return len(s) == len(g) and g in s+s

rotateString(s = "ckahkzpikz", goal = "hkzpikzcka")