from typing import List

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int: 

    if sum(gas) < sum(cost):
        return -1

    #sol exists
    res = 0
    total = 0
    for i in range(len(gas)):
        total += (gas[i] - cost[i])
        if total < 0:
            res = i+1
            total = 0
    return res


canCompleteCircuit(gas = [2,3,4], cost = [3,4,3])