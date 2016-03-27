# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param inorder : list of integers denoting inorder traversal
	# @param postorder : list of integers denoting postorder traversal
	# @return the root node in the tree
	def buildTree(self, inorder, postorder):
		if not inorder or not postorder:
			return None
		
		root = TreeNode(postorder.pop())
		root_index = inorder.index(root.val)
		
		leftNodes = inorder[:root_index]
		rightNodes = inorder[root_index+1:]

		# order matters
		root.right = self.buildTree(rightNodes, postorder)
		root.left = self.buildTree(leftNodes, postorder)
		
		return root