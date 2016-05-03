
class Solution:
	# @param A : tuple of integers
	# @return an integer
	def repeatedNumber(self, A):
		n = len(A)
		k = 3
		count = [0]*(k-1)
		cand = [-1]*(k-1)
		for i in xrange(n):
			j = 0
			# A[i] is checked if in cands
"""
You’re given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.

If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Example :

Input : [1 2 3 1 1]
Output : 1 
1 occurs 3 times which is more than 5/3 times. 
"""