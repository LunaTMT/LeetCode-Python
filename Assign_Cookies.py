def findContentChildren(self, g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    
    cookie = child = 0
    content = 0

    while cookie < len(s) and child < len(g):
        if s[cookie] >= g[child]:
            content += 1
            cookie, child = cookie+1, child+1
        else:
            cookie += 1

    return content