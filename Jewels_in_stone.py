
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        jewels = {i: 1 for i in [*jewels]}
        count = 0
        for stone in stones:
            if jewels.get(stone, False): count += 1
        return count
