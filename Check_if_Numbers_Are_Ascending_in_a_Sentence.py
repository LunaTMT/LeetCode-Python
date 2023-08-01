def areNumbersAscending( s: str) -> bool:
    s = s.split()
    numbers = [item for item in s if item.isdigit()]

    for i in range(1, len(numbers)):
        if not numbers[i-1] < numbers[i]:
            return False
    return True
    
areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles")