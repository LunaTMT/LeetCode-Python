class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(t) != len(s):
            return False
        
        for c in set(s):
            if t.count(c) != s.count(c):
                return False
        return True
                
