class Solution(object):

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        range_set = set(range(len(nums) + 1))
        num_set = set(nums)

        return list(range_set - num_set)[0]
