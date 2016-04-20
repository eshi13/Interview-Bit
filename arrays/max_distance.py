class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maximumGap(self, A):
		maxDistance = 0
		for i in xrange(len(A)):

			for j in xrange(i+1,len(A)):
				if A[i] <= A[j]:
					distance = j-i
					maxDistance = max(maxDistance,distance)
			return maxDistance



"""
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

If there is no solution possible, return -1.

Example :

A : [3 5 4 2]

Output : 2 
for the pair (3, 4)
"""