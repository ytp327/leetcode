<h1> 99. Recover Binary Search Tree --Hard</h1> 
<p>You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.</p>
<p>Follow up: A solution using <code>O(n)</code> space is pretty straight forward. Could you devise a constant space solution?</p>

<pre>
<b>Example1:</b>
<img src = "../pic/recover1.jpg" >
Input: 4
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
<b>Example2:</b>
<img src = "../pic/recover2.jpg" >
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
</pre>

``` python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.preNode = TreeNode(-float('inf'))
        self.first, self.second = None, None
        self.traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val
    
    def traverse(self, node):
        if not node: return
        self.traverse(node.left)
        if not self.first and self.preNode.val > node.val:
            self.first = self.preNode
        if self.first and self.preNode.val > node.val:
            self.second = node
        self.preNode = node
        self.traverse(node.right)
```