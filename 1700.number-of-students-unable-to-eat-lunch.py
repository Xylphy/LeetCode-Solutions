#
# @lc app=leetcode id=1700 lang=python
#
# [1700] Number of Students Unable to Eat Lunch
#

# @lc code=start
class Solution(object):
    def countStudents(self, students, sandwiches):
        from collections import Counter
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        counter_students = Counter(students)
        
        for sandwich in sandwiches:
            if counter_students[sandwich] == 0:
                return counter_students[1] + counter_students[0]
            counter_students[sandwich] -= 1

        return 0
        
        
# @lc code=end

