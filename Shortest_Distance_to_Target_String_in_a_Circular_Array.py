def closetTarget(words: list[str], target: str, s: int) -> int:
    n = len(words)
    i = s+n
    j = s
    count = 0
    while i > s and j < s+n:
        if words[i%n] == target or words[j%n] == target:
            return count
        count += 1
        i -= 1
        j += 1
    return -1
        
words = ["hello","i","am","leetcode","hello"]
target = "hello"
s = 1
closetTarget(words, target, s)