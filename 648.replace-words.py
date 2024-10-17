#
# @lc app=leetcode id=648 lang=python
#
# [648] Replace Words
#

# @lc code=start
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_word = True

    def search_prefix(self, word):
        node = self.root
        prefix = ""
        for char in word:
            if char not in node.children:
                break
            prefix += char
            node = node.children[char]
            if node.is_word:
                return prefix
        return word


class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()

        for word in dictionary:
            trie.insert(word)

        return " ".join(trie.search_prefix(word) for word in sentence.split())




# @lc code=end
