def longestCommonPrefix(self, strs: list[str]) -> str:
    strs.sort()
    pref = ""
    
    for i in range(len(strs[0])):
        if strs[0][i] == strs[-1][i]:
            pref += strs[0][i]
        else:
            break
    return pref
    
""" When sorted lexicographically the first and last string have the most variation in their prefixes. Everything between them will be closer to the first value. 
Therefore we only need to search the prefix of the first and last element to find the LCM.

The last being our most deviated word from initial will give us the largest possible match (i.e LCM)
