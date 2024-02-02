from typing import List

def asteroidCollision(arr: List[int]) -> List[int]:
    s = []
    for a in arr:
        while s and s[-1] > 0 and a < 0:
            if s[-1] + a < 0: s.pop()
            elif s[-1] + a > 0: break    
            else: s.pop(); break
        else: s.append(a)        
    return s


asteroidCollision(arr = [10,2,-5])