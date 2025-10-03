#
# @lc app=leetcode id=1455 lang=python3
#
# [1455] Check If a Word Occurs As a Prefix of Any Word in a Sentence
#


# @lc code=start
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        return next(
            (i + 1 for i, w in enumerate(sentence.split()) if w.startswith(searchWord)),
            -1,
        )


# @lc code=end
