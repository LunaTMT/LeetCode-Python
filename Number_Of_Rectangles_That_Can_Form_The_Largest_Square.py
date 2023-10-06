def countGoodRectangles(rectangles: list[list[int]]) -> int:
    lengths = [min(rect) for rect in rectangles]
    return lengths.count(max(lengths))