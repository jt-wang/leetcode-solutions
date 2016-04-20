
function TreeNode(val) {
      this.val = val;
      this.left = this.right = null;
  }

var rob = function (root) {
  return getValue(root);
};

//动态规划方程
//
function getValue(node) {
  if (node === null)
    return 0;
  if ((node.left === null) && (node.right === null))
    return node.val;
  if ((node.left === null) && (node.right !== null))
    return Math.max(getValue(node.right), (getValue(node.right.left) +
      getValue(node.right.right) + node.val));

  if ((node.left !== null) && (node.right === null))
    return Math.max(getValue(node.left), (getValue(node.left.left) +
      getValue(node.left.right) + node.val));

  var value_of_children = getValue(node.left)+getValue(node.right);
  var left =  getValue(node.left.left) + getValue(node.left.right);
  var right = getValue(node.right.left) + getValue(node.right.right);
  var self =  node.val;
  var value_of_grandchildren_and_self = left+right+self;
  var result = Math.max(value_of_children, value_of_grandchildren_and_self);
  return result;
}

var root = new TreeNode(3);
root.left = new TreeNode(2);
root.left.right = new TreeNode(3);
root.right = new TreeNode(3);
root.right.right = new TreeNode(1);
console.log(rob(root));
