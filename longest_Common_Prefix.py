def longestCommonPrefix(self, strs: list[str]) -> str:
    strs.sort()
    pref = ""
    
    for i in range(len(strs[0])):
        if strs[0][i] == strs[-1][i]:
            pref += strs[0][i]
        else:
            break
    return pref
    