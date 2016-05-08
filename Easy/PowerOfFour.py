import re


class Solution(object):

    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        num_str = ''
        if num is None:
            return False

        if num <= 0:
            return False

        if num == 1:
            return True

        num_str = bin(num)[2:]

        if len(num_str) >= 3:
            pattern = re.compile(r'^(00)+$')
            if pattern.match(num_str[1:]):
                return True
            else:
                return False
        else:
            return False
