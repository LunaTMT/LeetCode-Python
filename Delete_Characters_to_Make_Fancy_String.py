def makeFancyString(s: str) -> str:
    ans, last, count = [], "", 0
    for ch in s:
        if ch == last:
            count += 1
        else:
            count = 0
        if count < 2:
            ans.append(ch)
        last = ch
    return "".join(ans)

makeFancyString("leeetcode")