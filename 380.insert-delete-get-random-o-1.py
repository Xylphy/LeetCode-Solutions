#
# @lc app=leetcode id=380 lang=python
#
# [380] Insert Delete GetRandom O(1)
#


# @lc code=start
import random

class RandomizedSet(object):

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            return False

        self.list.append(val)
        self.dict[val] = len(self.list) - 1
        return True
            

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            return False

        idx, last = self.dict[val], self.list[-1]
        self.list[idx], self.dict[last] = last, idx
        self.list.pop()
        del self.dict[val]

        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
