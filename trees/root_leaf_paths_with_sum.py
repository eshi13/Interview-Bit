# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def pathSum(self, root, num):
		self.paths = []

		if root.left:
			self.checkPath(root.left, num, root.val, [root.val])
		if root.right:
			self.checkPath(root.right, num, root.val, [root.val])
		return self.paths

	def checkPath(self, node, num, current_val, path):
		if num == current_val + node.val and node.left is None and node.right is None:
			self.paths.append(path + [node.val])
			return
		if node.left:
			self.checkPath(node.left, num, current_val + node.val, path + [node.val])
		if node.right:
			self.checkPath(node.right, num, current_val + node.val, path + [node.val])


"""
Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals the given sum.

For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return

[
   [5,4,11,2],
   [5,8,4,5]
]

22-5 = 17
17-4 = 13
13-11 = 2
2-2 = 0
"""