def maximumUnits(boxes: list[list[int]], truckSize: int) -> int:
    boxes.sort(lambda x:x[1], reverse=1)
    s = 0
    for i, j in boxes:
        i = min(i, truckSize)
        s = i * j
        truckSize -= i

        if truckSize == 0:
            break
    return s 

maximumUnits(boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10)