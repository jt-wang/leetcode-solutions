/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean hasPathSum(TreeNode root, int sum) {
        //对所有路径查找，如果该路径相等，则返回true.
        if(root == null){
            return false;
        }
        else if(root.left == null && root.right == null){
            //如果到了叶节点
            return (root.val == sum)? true:false;
        }
        
        else return (hasPathSum(root.left, sum-root.val) || hasPathSum(root.right, sum-root.val));
    }
}