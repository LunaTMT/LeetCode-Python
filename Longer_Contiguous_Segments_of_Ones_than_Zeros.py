
def checkZeroOnes(s: str) -> bool:
    best_one = one_count = best_zero = zero_count = 0
    
    for c in s:
        if c == "1":
            one_count += 1
            zero_count = 0
        else:
            one_count = 0
            zero_count += 1
    
        best_one = max(best_one, one_count)
        best_zero = max(best_zero, zero_count)

    return best_one > best_zero

checkZeroOnes("01111110")   