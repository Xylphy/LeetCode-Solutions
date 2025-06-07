#
# @lc app=leetcode id=3170 lang=python
#
# [3170] Lexicographically Minimum String After Removing Stars
#


# @lc code=start
class Solution(object):
    def clearStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        map = [[] for _ in range(26)]
        s_list = list(s)

        for i, c in enumerate(s):
            if c == "*":
                for j in range(26):
                    if map[j]:
                        s_list[map[j].pop()] = ""
                        break
                s_list[i] = ""
            else:
                map[ord(c) - ord("a")].append(i)

        return "".join(s_list)


# @lc code=end
