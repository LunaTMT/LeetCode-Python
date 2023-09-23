def findTheLongestBalancedSubstring(s: str) -> int:
    
    #harsh_negi_07
    res, temp = 0, "01"
    while len(temp) <= len(s):
        if temp in s: 
            res = len(temp)
        temp = '0' + temp + '1'
    return res
    
    
    #OR
    # olzh06

    """ 
    tmp = '01'
    while tmp in s:
        tmp = '0' + tmp + '1'
    return len(tmp) - 2
    """

findTheLongestBalancedSubstring("01000111")