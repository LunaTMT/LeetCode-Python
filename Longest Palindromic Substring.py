def longest_palindromic_substring(s):
    if not s:
        return ""

    # Preprocess the string to handle even-length palindromes
    processed_str = '#'.join('^{}$'.format(s))

    n = len(processed_str)
    p = [0] * n  # Array to store the palindrome lengths

    center, right = 0, 0  # Current center and its corresponding right boundary

    for i in range(1, n - 1):
        # Mirror index calculation
        mirror = 2 * center - i

        # Check if the current index is within the current palindrome boundary
        if right > i:
            p[i] = min(right - i, p[mirror])

        # Attempt to expand the palindrome centered at i
        while processed_str[i + (1 + p[i])] == processed_str[i - (1 + p[i])]:
            p[i] += 1

        # Update the center and right boundary if needed
        if i + p[i] > right:
            center, right = i, i + p[i]

    # Find the maximum palindrome length and its center
    max_len, center_index = max((length, index) for index, length in enumerate(p))

    # Retrieve the original palindrome from the processed string
    start = (center_index - max_len) // 2
    end = start + max_len - 1
    return s[start:end + 1]

# Example usage
input_string = "babad"
result = longest_palindromic_substring(input_string)
print(result)
