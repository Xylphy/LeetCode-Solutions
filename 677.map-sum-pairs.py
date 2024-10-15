#
# @lc app=leetcode id=677 lang=python
#
# [677] Map Sum Pairs
#

from collections import defaultdict


# @lc code=start
class MapSum(object):

    class TrieNode:
        def __init__(self):
            self.children = defaultdict(MapSum.TrieNode)
            self.value = 0

    def __init__(self):
        self.root = self.TrieNode()
        self.seen = defaultdict(int)

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        curr = self.root
        for c in key:
            curr = curr.children[c]
            curr.value += val - self.seen.get(key, 0)

        self.seen[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return 0
            curr = curr.children[c]

        return curr.value


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# @lc code=end
