from collections import Counter

def maxNumberOfBalloons(self, text: str) -> int:
    txt_count = Counter(text)
    balloon_count = Counter("balloon")

    res = len(text)
    for i in balloon_count:
        res = min(res, txt_count[i] // balloon_count[i]) 

    return res