def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for i, w in enumerate(strs):     
        res["".join(sorted(w))].append(w)
    return res.values()

