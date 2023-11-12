import heapq
def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        
        for (x, y) in points:
            dist = -(x*x + y*y)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [(x,y) for (dist,x, y) in heap]

kClosest(points = [[3,3],[5,-1],[-2,4],[5, 5],[1,1]], k = 2)


"""
res = [(sqrt(p[0]**2 + p[1]**2), p) for p in points]
return [p[1] for p in sorted(res)[:k]]
"""