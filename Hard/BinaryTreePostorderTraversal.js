 'use strict';
  function TreeNode(val) {
      this.val = val;
      this.left = this.right = null;
  }

/**
 * Definition for a binary tree node.

/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var pre = function(node) {
  if (node !== null) {
    var stack = [];
    stack.push(node);
    while (stack.length > 0) {
      node = stack.pop();
      console.log(node.val);
      if (node.right !== null)
        stack.push(node.right);
      if (node.left !== null)
        stack.push(node.left);
    }
 }
}

var mid = function(node) {
  if (node !== null) {
    var stack = [];
    while (stack.length > 0 || node !== null) {
      if (node !== null) {
        stack.push(node);
        node = node.left;
      } else {
        node = stack.pop();
        console.log(node.val);
        node = node.right;
      }
    }
  }
}

var post = function(node) {
  if(node !== null) {
    var s1 = [];
    var s2 = [];
    s1.push(node);
    while (s1.length > 0) {
      node = s1.pop();
      s2.push(node);
      if(node.left !== null) {
        s1.push(node.left);
      }
      if (node.right !== null) {
        s1.push(node.right);
      }
    }

    while(s2.length > 0) {
      console.log(s2.pop().val);
    }
  }
}

var postorderTraversal_without_recursion = function(root) {
  var result = [];
  if (root === null)
    return result;
  var stack = [];
  stack.push(root);
  var temp = null;

  while (stack.length > 0) {
    temp = stack[stack.length-1];
    if (temp.left !== null && root !== temp.left && root !== temp.right) {
      stack.push(temp.left);
    } else if (temp.right !== null && root !== temp.right) {
      stack.push(temp.right);
    } else {
      result.push(stack.pop().val);
      root = temp;
    }
  }

  return result;
}


var postorderTraversal = function(root) {
    var result = [];
    function add_to_result(node) {
        var val_to_test = (new Object(node.val)).toString();
        if (val_to_test.match(/\d+/g)) {
            result.push(Number(val_to_test));
            return;
        }
    }
    
    function fn (node) {
    if (node === null) 
        return;
    if (node.left !== null)
      fn(node.left);
    if (node.right !== null)
      fn(node.right);

    add_to_result(node);
    }
    fn(root);
    
    return result;
};

var root = new TreeNode(1);
// root.left = new TreeNode('#');
root.right = new TreeNode(2);
root.right.left = new TreeNode(3);
post(root);
//console.log(postorderTraversal_without_recursion(root));

