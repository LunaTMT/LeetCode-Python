import random

class RandomizedSet:

    def __init__(self):
       self.set_ = {}


    def insert(self, v: int) -> bool:
        if v in self.set_:
            return False
        else:
            self.set_[v] = 1
            return True

    def remove(self, v: int) -> bool:
        if v not in self.set_:
            return False
        else: 
            del self.set_[v]
            return True
        

    def getRandom(self) -> int:
        return random.choice(list(self.set_.keys()))

    
if __name__ == "__main__":
    randomizedSet = RandomizedSet()
    randomizedSet.insert(1)     #; // Inserts 1 to the set. Returns true as 1 was inserted successfully.
    randomizedSet.remove(2)     #; // Returns false as 2 does not exist in the set.
    randomizedSet.insert(2)     #; // Inserts 2 to the set, returns true. Set now contains [1,2].
    randomizedSet.getRandom()   #; // getRandom() should return either 1 or 2 randomly.
    randomizedSet.remove(1)     #// Removes 1 from the set, returns true. Set now contains [2].
    randomizedSet.insert(2)     #; // 2 was already in the set, so return false.
    randomizedSet.getRandom()   #; // Since 2 is the only number in the set, getRandom() will always return 2.