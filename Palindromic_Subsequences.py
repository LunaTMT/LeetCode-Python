import string

def countPalindromicSubsequence(s):
        
        count = 0
        for i in set(s):
                start, end = s.find(i), s.rfind(i)
                between = set(s[start+1:end])
                count += len(between)
        return count

if __name__ == "__main__":
     countPalindromicSubsequence("bbcbaba")
