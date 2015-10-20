/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class CountCompleteTreeNodes {

    public int getHeight(TreeNode node){
  


        int height = -1;
        while (node!=null) {
            height++;
            node = node.left;
        }
        return height;
    }

    public int countNodes(TreeNode root) {
        if (root == null){
            return 0;
        }

        TreeNode left = root, 
        TreeNode right = root;

        int height = 0;

        while (right != null) {
            left = left.left;
            right = right.right;
            height++;
        }

        if (left == null){
            //说明左右数高相等
            return (1 << height) - 1;
        }else{
        return 1 + countNodes(root.left) + countNodes(root.right);
    }
}

}              