# https://leetcode.com/problems/map-sum-pairs

class MapSum:
    def __init__(self):
        self.d = {}

    def __check__(self, prefix, key):
        if len(prefix) > len(key):
            return False
        for i in range(len(prefix)):
            if prefix[i] != key[i]:
                return False
        return True

    def insert(self, key, val):
        self.d[key] = val

    def sum(self, prefix):
        r = 0
        for key in self.d.keys():
            if self.__check__(prefix, key):
                r += self.d[key]
        return r

