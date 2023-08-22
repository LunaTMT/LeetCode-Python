def addBinary(self, A: str, B: str) -> str:

    if len(A) > len(B):
        B = B.zfill(len(A))
    else:
        A = A.zfill(len(B))

    C = deque([]) 
    carry = 0
    for (a, b) in  zip(A[::-1],B[::-1]):
        sum = int(a) + int(b) + carry
        C.appendleft(str(sum % 2))  
        carry = sum // 2 

    if carry == 1:
        C.appendleft("1")

    return "".join(C)