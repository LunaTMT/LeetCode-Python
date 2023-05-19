class MyHashMap:

    def __init__(self):
        self.data = []

    def put(self, key: int, value: int) -> None:

        found = False
        for idx, (k, _) in enumerate(self.data):
            if k == key:
                self.data[idx] = (key, value)
                found = True
                break
            
        if not found: self.data.append((key, value))
        

    def get(self, key: int) -> int:
        for (k, v) in self.data:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        for idx, (k, _) in enumerate(self.data):
            if k == key:
                del self.data[idx]
                break
if __name__ == "__main__":
    myHashMap = MyHashMap()
    myHashMap.put(1, 1); # The map is now [[1,1]]
    myHashMap.put(2, 2); # The map is now [[1,1], [2,2]]
    myHashMap.get(1);    # return 1, The map is now [[1,1], [2,2]]
    myHashMap.get(3);    # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
    myHashMap.put(2, 1); # The map is now [[1,1], [2,1]] (i.e., update the existing value)
    myHashMap.get(2);    # return 1, The map is now [[1,1], [2,1]]
    myHashMap.remove(2); # remove the mapping for 2, The map is now [[1,1]]
    myHashMap.get(2);    # return -1 (i.e., not found), The map is now [[1,1]]