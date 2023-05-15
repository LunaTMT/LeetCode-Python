class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        length = 0

        for i in reversed(s.rstrip()):
            if i != " ":
                length += 1
            else:
                break
        return length