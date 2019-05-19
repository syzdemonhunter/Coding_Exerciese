# https://leetcode.com/problems/unique-email-addresses/
# https://www.jiuzhang.com/solution/unique-email-addresses/#tag-highlight-lang-python
# T：O(n)
# S: O(n)

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result = set()
        for email in emails:
            local, domain = email.split('@')
            local = ''.join(local.split('+')[0].split('.'))
            email = local + '@' + domain
            result.add(email)
        return len(result)