class OrderedStream:

    def __init__(self, n: int):
        self.arr = [0] * n
        self.n = n
        self.ptr = 0

    def insert(self, id: int, value: str) -> list[str]:
        id -= 1
        self.arr[id] = value

        if id > self.ptr: return []

        while self.ptr < self.n and self.arr[self.ptr]:
            self.ptr += 1

        return self.arr[id:self.ptr]




o = OrderedStream(5)
o.insert(3, "c")
o.insert(1, "a")
o.insert(2, "b")
o.insert(5, "e")
o.insert(4, "d")



