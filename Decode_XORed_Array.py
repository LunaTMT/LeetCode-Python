

def decode(encoded: list[int], first: int) -> list[int]:
    arr=[first]
    temp=0
    for i in encoded:
        temp=i^first
        arr.append(temp)
        first=temp
    return arr

decode(encoded = [6,2,7,3], first = 4)