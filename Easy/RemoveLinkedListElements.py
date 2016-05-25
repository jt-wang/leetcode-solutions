# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        sequence = []
        while head is not None:
            sequence.append(head)
            head = head.next

        result_sequence = list(filter(lambda x: x.val != val, sequence))
        # print(len(result_sequence))
        if not result_sequence:
            return None

        if len(result_sequence) == 1:
            result_sequence[0].next = None
            return result_sequence[0]

        for i in range(len(result_sequence) - 1):
            result_sequence[i].next = result_sequence[i + 1]

        result_sequence[-1].next = None
        return result_sequence[0]

head = ListNode(1)
head.next = ListNode(2)
given_val = 2

s = Solution()
result = s.removeElements(head, given_val)
while result is not None:
    print(result.val)
    result = result.next
