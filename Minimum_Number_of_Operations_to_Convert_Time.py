def convertTime( current: str, correct: str) -> int:
    current_time = 60 * int(current[:2]) + int(current[-2:]) # Current time in minutes
    target_time = 60 * int(correct[:2]) + int(correct[-2:])
    diff = target_time - current_time 
    operations = 0

    for i in (60, 15, 5, 1):
        operations += diff // i
        diff %= i
    return operations

convertTime(current="02:30" , correct="04:10")