from typing import List
from collections import defaultdict
def accountsMerge(arr: List[List[str]]) -> List[List[str]]:
    AL = defaultdict(list)
    visited = [False] * len(arr)
    res = []

    for i, acc in enumerate(arr):
        for j in range(1, len(acc)):
            AL[acc[j]].append(i)

    def dfs(i, emails):
        if visited[i]:
            return
        visited[i] = True

        for j in range(1, len(arr[i])):
            email = arr[i][j]
            emails.add(email)
            for neighbour in AL[email]:
                dfs(neighbour, emails)
    
    for i, acc in enumerate(arr):
        if visited[i]:
            continue
        name, emails = acc[0], set()
        dfs(i, emails)
        res.append([name] + sorted(emails))
    return res

accountsMerge( arr = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])