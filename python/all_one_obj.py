#!/usr/bin/env python3

from collections import defaultdict
class AllOne:

# /** Initialize your data structure here. */
    def __init__(self, allone: dict):
        self.allone = defaultdict(int)

    # /** Inserts a new key <Key> with value 1. Or increments an existing key by 1. */
    def inc(self, key):
        self.inc = self.allone[key] += 1

    # /** Decrements an existing key by 1. If Key's value is 1, remove it from the data structure. */
    def dec(self, key):
        if not self.allone:
            raise Exception
        if self.allone[key] == 1:
            del self.allone[key]
        else:
            self.dec = self.allone[key] -= 1

    # /** Returns one of the keys with maximal value. */
    def getMaxKey(self): 
        if not self.allone:
            raise Exception
        result = None
        for key, value in self.allone.items():
            if result is None:
                result = key
            elif result < key:
                result = key
        return result
        # self.allone.sort(key=lambda x: -x)[0] O(n log n)

    # /** Returns one of the keys with Minimal value. */
    def getMinKey(self):
        # self.allone.sort(key=lambda x: x)[0] O(n log n)
        if not self.allone:
            raise Exception
        result = None
        for key, value in self.allone.items():
            if result is None:
                result = key
            elif result > key:
                result = key
        return result
        # self.allone.sort(key=lambda x: x)[0] O(n log n)

# /**
# * Your AllOne object will be instantiated and called as such:
# * var obj = new AllOne()
# * obj.inc(key)
# * obj.dec(key)
# * var param_3 = obj.getMaxKey()
# * var param_4 = obj.getMinKey()
# */