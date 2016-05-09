# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack_ = []
        while root is not None or stack_:
            while root is not None:
                stack_.append(root)
                # print(root.val)
                root = root.left
            if stack_:
                root = stack_.pop()
                print(root.val)
                result.append(root.val)
                root = root.right

        return result

s = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(s.inorderTraversal(root))
