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
    def preorderTraversal(self, A):
    	res = []
    	stack = []
    	if A is None:
    		return res
    	stack.insert(0, A)
    	while len(stack):
    		node = stack.pop()
    		res.append(node.val)
    		if node.left != None:
    			stack.insert(0,node.left)
    		if node.right != None:
    			stack.insert(0,node.right)
		return res

