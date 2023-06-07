class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        if len(w1) > len(w2):
            large = w1
            small = w2
        else: 
            large = w2
            small = w1

        small = len(small)

        res = ""
        for i in range(small):
            res += w1[i] + w2[i]
        
        return res + large[small:]
           