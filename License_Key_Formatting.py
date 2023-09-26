def licenseKeyFormatting(s: str, k: int) -> str:
    s = s.replace('-', '')
    head = len(s) % k 
    grouping = []
    
    if head:
        grouping.append(s[:head])
    
    for i in range(head, len(s), k):
        grouping.append(s[i : i+k])
    
    return '-'.join(grouping).upper()

    "or"
    
    s = s.lstrip("-")
    n = len(s)-1
    res = ""
    j = 0
    for i in range(n, -1, -1):
        
        if j % k == 0 and res and res[-1] != "-" and i != n:
            res += "-"
           
        if s[i] != "-":
            res += s[i].upper()
            j += 1

    return res



s = "5F3Z-2e-9-w"
k = 4

licenseKeyFormatting(s, k)