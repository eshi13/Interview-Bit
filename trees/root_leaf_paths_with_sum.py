# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
	def hasPathSum(self, A, B):
		if A is None:
			return 0
		if A.val == B and A.left is None and A.right is None:
			return 1	# successful
		return self.hasPathSum(A.left, B-A.val) or self.hasPathSum(A.right, B-A.val)

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