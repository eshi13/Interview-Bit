# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root : root node of tree
	# @param val1 : integer
	# @param val2 : integer
	# @return an integer
	def lca(self, root, val1, val2):
		s1, s2 = [], []

		if self.path(root, s1, val1) == False or self.path(root, s2, val2) == False:
			return -1
		i = 0
		while i < len(s1) and i < len(s2):
			if s1[i] != s2[i]:
				break
			i += 1
		return s1[i-1]
	def path(self, root, s, val):
		if root == None:
			return False
		s.append(root.val)
		if root.val == val:
			return True
		if (root.left != None and self.path(root.left,s,val) or (root.right != None and self.path(root.right,s,val))):
			return True
		s.pop()
		return False