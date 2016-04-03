class Solution:
	# @param A : list of integers
	# @return an integer
	def removeDuplicates(self, A):
		count = 0
		for i in xrange(0, len(A)):
			if i < len(A)-2 and A[i] == A[i+1] and A[i] == A[i+2]:
				continue
			else:
				A[count] = A[i]
				count += 1
		A = A[:count]
		return count
"""
 0  1  2  3  4  5  6
[2, 4, 6, 6, 6, 7, 7]
count = 2
i = 2
i = 3
A[2] = 6
count = 3
i = 4
A[3] = 6
count = 4
A[4] = 7
A[5] = 7
"""