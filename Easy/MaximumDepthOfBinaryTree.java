/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
//divide and conquer
public class Solution {
    public int maxDepth(TreeNode root) {
        if(root == null){
            return 0;
        }else {
        int leftDepth = 1+maxDepth(root.left);
        int rightDepth = 1+maxDepth(root.right);
        return (leftDepth >= rightDepth)?leftDepth:rightDepth;
        }
    }

}