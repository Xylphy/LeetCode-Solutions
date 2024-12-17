#
# @lc app=leetcode id=929 lang=python
#
# [929] Unique Email Addresses
#

# @lc code=start
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_addresses = {}

        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            email = local + '@' + domain
            email_addresses[email] = True

        return len(email_addresses)
        
# @lc code=end

