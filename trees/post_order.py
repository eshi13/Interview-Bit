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
    	res = []
    	stack = []
    	if A is None:
    		return res
    	stack.insert(0, A)
    	while len(stack):
    		node = stack.pop()
    		res.append(node.val)
    		if node.left:
    			stack.insert(0,node.left)
    		if node.right:
    			stack.insert(0,node.right)
		return res.reverse()


"""
2.1. pop an item from the stack and print it.

2.2. push the left child of popped item to stack.

2.3. push the right child of popped item to stack.

reverse the ouput.
"""