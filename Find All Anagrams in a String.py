class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        sCount, pCount = defaultdict(int), Counter(p)

        for i in range(len(p)):
            sCount[s[i]] += 1
        
        res = [0] if sCount == pCount else []
        l = 0

        for r in range(len(p), len(s)):
            sCount[s[l]] -= 1
            sCount[s[r]] += 1

            if sCount[s[l]] == 0:
                sCount.pop(s[l])

            if sCount == pCount:
                res.append(l+1)

            l += 1
        return res


