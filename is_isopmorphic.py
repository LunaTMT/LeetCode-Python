def isIsomorphic(s: str, t: str) -> bool:
    ST = {}
    TS = {}

    if len(s) < len(t) or len(t) < len(s):
        return False

    for s, t in zip(s, t):
        if (s in ST and ST[s] != t) or  (t in TS and TS[t] != s): return False
        else: 
            ST[s] = t
            TS[t] = s
    return True

if __name__ == "__main__":
    isIsomorphic("egg", "add")
