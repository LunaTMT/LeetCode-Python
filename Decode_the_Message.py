def decodeMessage(self, key: str, message: str) -> str:
    lookup = {}
    lookup[" "] = " "
    res = ""
    alphabet = list(range(97, 123))
    
    i = 0
    for c in key:
        if c not in lookup:
            lookup[c] = chr(alphabet[i])
            i += 1

    for c in message:
        res += lookup[c]
    return res

key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"

decodeMessage(key, message)