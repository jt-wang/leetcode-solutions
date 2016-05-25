class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set()
        l = len(nums)
        for index, num in enumerate(reversed(nums)):
            if num in num_set:
                del nums[l - index - 1]
            else:
                num_set.add(num)

        return len(nums)

print(Solution().removeDuplicates([1, 2, 3, 4]))

'''
Attention: all of the 'solution' that is not implemented by reversed/backward deleting are wrong.
Because the index/iterator depends on the original length.
'''
