def reformat(self, s: str) -> str:

    large = digits = [c for c in s if c.isdigit()]
    small = letters = [c for c in s if c.isalpha()]

    d = len(digits)
    l = len(letters)

    if abs(d - l) > 1:
        return ""

    if d < l:
        small = digits
        large = letters

    return "".join([l+c for l, c in zip(large, small)] +  large[len(small):])
