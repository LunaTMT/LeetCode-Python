def isValid(s):
        if len(s) % 2 != 0: #If there are an odd number of brackets then we know it is false automatically
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

        
        
        start = s[0]
        middle = []
        close = pairs[start]
        s = s[1:]

        while True:
            for i, char in enumerate(s):
                if char == close:
                    
                    count = [middle.count(char) for char in set(middle)]
                
                    for item in count:
                        if item % 2 == 0:
                            return False
                    break
                else:
                    middle.append(char)
   
       
       


if __name__ == "__main__":
        isValid("([}}])")

        #([])(())({})([])