#
# @lc app=leetcode id=1160 lang=python
#
# [1160] Find Words That Can Be Formed by Characters
#

# @lc code=start
class Solution(object):
    def countCharacters(self, words, chars):
        from collections import Counter
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        total_length = 0

        chars_counter = Counter(chars)

        for word in words:
            word_counter = Counter(word)
            for key in word_counter:
                if word_counter[key] > chars_counter[key]:
                    break
            else:
                total_length += len(word)

        return total_length

        
# @lc code=end

