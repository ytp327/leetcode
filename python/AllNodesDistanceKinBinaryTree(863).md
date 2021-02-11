<h1> 863. All Nodes Distance K in Binary Tree --Medium</h1> 
<p>We are given a binary tree (with root node root), a target node, and an integer value K.</p>
<p>Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.</p>

<pre>
<b>Example 1:</b>
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
Output: [7,4,1]
Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.
<img src = "../pic/NodeKDistance.png" >
Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
</pre>

<p>Approach 1 (DP, O(n<sup>2</sup>)):</p>
``` python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        adjList, stack = collections.defaultdict(list), [root]
        level, seen = set(), set()
        while stack:
            node = stack.pop()
            if node == target:
                level.add(node)
            if node.left:
                stack.append(node.left)
                adjList[node.left].append(node)
                adjList[node].append(node.left)
            if node.right:
                stack.append(node.right)
                adjList[node.right].append(node)
                adjList[node].append(node.right)

        while K:
            temp, level = level, set()
            for node in temp:
                seen.add(node)
                for adjNode in adjList[node]:
                    if adjNode not in seen:
                        level.add(adjNode)
            K -= 1
        return [node.val for node in level]
```