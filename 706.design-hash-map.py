#
# @lc app=leetcode id=706 lang=python
#
# [706] Design HashMap
#

# @lc code=start
class MyHashMap(object):

    def __init__(self):
        self.hash_set = [None] * (pow(10, 6) + 1)
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.hash_set[key] = value
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        return self.hash_set[key] if self.hash_set[key] is not None else -1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hash_set[key] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

