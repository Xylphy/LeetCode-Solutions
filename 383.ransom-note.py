#
# @lc app=leetcode id=383 lang=python
#
# [383] Ransom Note
#

# @lc code=start
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        from collections import Counter
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counter_ransom_note = Counter(ransomNote)
        counter_magazine = Counter(magazine)

        return all(counter_ransom_note[k] <= counter_magazine[k] for k in counter_ransom_note)

        
# @lc code=end

