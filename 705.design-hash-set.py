#
# @lc app=leetcode id=705 lang=python
#
# [705] Design HashSet
#

# @lc code=start
class MyHashSet(object):

    def __init__(self):
        self.hash_set = [None] * (pow(10, 6) + 1)

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hash_set[key] = key

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hash_set[key] = None

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return self.hash_set[key] != None
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

