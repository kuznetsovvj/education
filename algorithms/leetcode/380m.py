# https://leetcode.com/problems/insert-delete-getrandom-o1/

import random

class RandomizedSet:
    def __init__(self):
        self.lst = []
        self.dct = {}

    def insert(self, val: int) -> bool:
        if val in self.dct:
            return False
        self.lst.append(val)
        self.dct[val] = len(self.lst) - 1
        return True        

    def remove(self, val: int) -> bool:
        if val not in self.dct:
            return False
        t = self.dct[val]
        del self.dct[val]
        for i in range(t+1, len(self.lst)):
            self.dct[self.lst[i]] -= 1
        del self.lst[t]
        return True
        
    def getRandom(self) -> int:
        return self.lst[random.randint(0, len(self.lst)-1)]
    
a = RandomizedSet()
print("insert 1", a.insert(1))
print("remove 2", a.remove(2))
print("insert 2", a.insert(2))
print("random", a.getRandom())
print("remove 1", a.remove(1))
print("insert 2", a.insert(2))
print("random", a.getRandom())