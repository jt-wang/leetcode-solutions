class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None:
            return s

        if len(s) == 0:
            return s

        return s[::-1]
