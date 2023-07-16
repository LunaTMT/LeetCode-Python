def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

    index = {"type": 0,
            "color": 1,
            "name" : 2}
    type_idx = index[ruleKey]
    res = 0
    for item in items:
        if item[type_idx] == ruleValue:
            res += 1
    return res