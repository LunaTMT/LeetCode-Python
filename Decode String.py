def decode_string(s):
    stack = []
    current_str = ""
    current_count = 0

    for char in s:
        if char.isdigit():
            current_count = current_count * 10 + int(char)
        elif char == '[':
            stack.append((current_count, current_str))
            current_count = 0
            current_str = ""
        elif char == ']':
            count, prev_str = stack.pop()
            current_str = prev_str + count * current_str
        else:
            current_str += char

    return current_str


# Example 2


input_str2 = "3[a]2[bc]"
output2 = decode_string(input_str2)
print(output2)  # Output: "accaccacc"


