def separateDigits(self, nums: List[int]) -> List[int]:
    return [int(digit) for n in nums for digit in str(n)]
    
    "or simply"
    answer = []
    for item in nums:
        answer.extend(list(map(int, str(item))))
    return answer
