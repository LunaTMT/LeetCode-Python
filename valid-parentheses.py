def isValid(s):
        if len(s) % 2 != 0: 
            return False
        
        if s[0] not in ["(", "[", "{"]:
            return False
        
        pairs = {
            "(" : ")",
            ")" : "(",
            "[" : "]",
            "]" : "[",
            "{" : "}",
            "}" : "{",
        }

        open = []

        for c in s:
            if c in ["(", "[", "{"]:
                open.append(c)            
            elif open:
                if c == pairs[open[-1]]:
                    open.pop()         
            else:
                return False
        return True if not open else False


if __name__ == "__main__":
        isValid("([}}])")

        #([])(())({})([])
