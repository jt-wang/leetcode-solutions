function TreeNode (val) {
this.val = val;
this.left = this.right = null;
}

var isSameTree = function (p, q) {
//一层一层地向下判断，在任何一层不一样就 false。一直到最后都一样才true
//确定边界条件:
  if (p === null && q === null)
    return true;
  if (p === null && q !== null)
    return false;
  if (p !== null && q === null)
    return false;

  if (p.val === q.val) {
    return (isSameTree(p.left, q.left) && isSameTree(p.right, q.right));
  } else {
    return false;
  }
};

var root1 = new TreeNode(3);
root1.left = new TreeNode(5);
root1.right = new TreeNode(5);
var root2 = new TreeNode(3);
root2.left = new TreeNode(5);
console.log(isSameTree(root1, root2));
