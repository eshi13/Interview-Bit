# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
	def sumNumbers(self, A):
		return self.sumNum(A, 0)
	def sumNum(A, currentSum):
		if A is None:
			return currentSum
		currentSum = (currentSum * 10 + A.val) % 1003
		
		if A.left is None and A.right is None:
			return currentSum
		if A.left is None:
			return self.sumNum(A.right, currentSum)
		if A.right is None:
			reutrn self.sumNum(A.left, currentSum)
		return (self.sumNum(A.left, currentSum) + self.sumNum(A.right, currentSum)) % 1003
