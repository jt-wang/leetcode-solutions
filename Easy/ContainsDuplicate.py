class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None:
            return False
        if len(nums) == 0:
            return False

        set_of_nums = set()
        for num in nums:
            if num in set_of_nums:
                return True
            else:
                set_of_nums.add(num)

        return False
