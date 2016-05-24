class Solution(object):

    def get_intersection_when_l1_smaller_than_l2(self, l1, l2):
        result = []
        map_of_l1 = {}
        for x in l1:
            if x in map_of_l1:
                map_of_l1[x] += 1
            else:
                map_of_l1[x] = 1

        for y in l2:
            if y in map_of_l1:
                result.append(y)
                map_of_l1[y] -= 1
                if map_of_l1[y] == 0:
                    del map_of_l1[y]
        return result

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 and nums2:
            if len(nums1) <= len(nums2):
                return self.get_intersection_when_l1_smaller_than_l2(nums1, nums2)
            else:
                return self.get_intersection_when_l1_smaller_than_l2(nums2, nums1)
        else:
            return []
