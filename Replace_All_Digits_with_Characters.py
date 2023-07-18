#https://leetcode.com/problems/replace-all-digits-with-characters/solutions/3782923/python-simplest-solution-with-detailed-explanation-beats-97-94/
def replaceDigits(self, s: str) -> str:
    s = [*s]
    for i in range(1, len(s), 2):
        s[i] = chr(ord(s[i-1]) + int(s[i]))
    return "".join(s)
