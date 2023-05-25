class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        gaps = {0 : 0}

        for row in wall:
            count = 0
            for brick in row[:-1]:
                count += brick
                gaps[count] = gaps.get(count, 0) + 1 
        

        return len(wall) - max(gaps.values())

      
  