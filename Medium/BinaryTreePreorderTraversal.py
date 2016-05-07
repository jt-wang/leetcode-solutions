# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def fn(self, result_list, root):
        if root is None:
            return

        if root.val is None:
            return

        result_list.append(root.val)
        # print(result_list)
        self.fn(result_list, root.left)
        self.fn(result_list, root.right)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result_list = []
        self.fn(result_list, root)
        return result_list
