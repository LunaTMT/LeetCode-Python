def reversePrefix(s: str, ch: str) -> str:
        for i in range(len(s)):
            if s[i] == ch: 
                return s[:i][::-1] + s[i+1:]
            
if __name__ == "__main__":
     reversePrefix("abcdefd", "d")