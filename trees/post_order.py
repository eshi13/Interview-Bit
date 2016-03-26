
class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def postorderTraversal(self, A):
		res, stack1, stack2 = [], [], []
		if A is None:
			return None
		stack1.append(A)
		while len(stack1) != 0:
			node = stack1.pop(0)
			stack2.insert(0, node)

			if node.left != None: 
				stack1.insert(0, node.left)
			if node.right != None:
				stack1.insert(0, node.right)
		while len(stack2) != 0:
			node = stack2.pop(0)
			res.append(node.val)
		return res


"""
2 stacks
"""