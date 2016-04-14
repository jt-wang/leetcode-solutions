function TreeNode(val) {
 this.val = val;
 this.left = this.right = null;
  }

var invertTree = function(root) {
    //对每个子node，都让它的子node反过来
    if (root === null){
        return null;
    } else if (root.left === null && root.right === null) {
        return root;
    } else {
        var temp = root.left;
        root.left = root.right;
        root.right = temp;
        invertTree(root.left);
        invertTree(root.right);
        return root;
    }

};
