# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        nodes.reverse()
        if nodes:
            if len(nodes) >= 2:
                for i in range(len(nodes) - 1):
                    nodes[i].next = nodes[i + 1]
                nodes[-2].next = nodes[-1]
                nodes[-1].next = None
                return nodes[0]
            else:
                return nodes[0]
        else:
            return None
