# Concept is there, see java for correct test cases
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def postorderTraversal(self, A):
		res, stack1, stack2 = [], [], []
		if A is None:
			return None
		stack1.append(A)
		while len(stack1) != 0:
			node = stack1.pop()
			stack2.insert(0, node)

			if node.left != None: 
				stack1.insert(0, node.left)
			if node.right != None:
				stack1.insert(0, node.right)
		while len(stack2) != 0:
			node = stack2.pop()
			res.append(node.val)
		return res


"""
2 stacks
"""