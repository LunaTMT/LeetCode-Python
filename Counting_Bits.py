def countBits(self, num: int) -> List[int]:
    """
    Uses the fact that multiplcation by 2 in binary is just shifting everything to the right one
    and parity theory
    
    2n      - EVEN
    2n + 1  - ODD

    Since multiplying by 2 just adds a zero, then any number and its double will have the same number of 1's. 
    Likewise, doubling a number and adding one will increase the count by exactly 1. 



    """
    counter = [0]
    for i in range(1, num+1):
        counter.append(counter[i >> 1] + i % 2)
    return counter  

    """
    Niave solution
    
    return [bin(i)[2:].count("1") for i in range(n+1)]
     
    """