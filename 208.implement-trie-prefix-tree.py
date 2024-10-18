#
# @lc app=leetcode id=208 lang=python
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Trie(object):
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.isEnd = False

    def __init__(self):
       self.root = Trie.TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie.TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.isEnd
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

