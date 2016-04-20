# Always switching ij = ji
# ji = ij
class Solution:
	# @param A : list of list of integers
	# @return the same list modified
	def rotate(self, A):
		for i in xrange(len(A)/2):
			for j in xrange(i, len(A)-1-i):
				temp = A[i][j]									# 00
				A[i][j] = A[len(A)-1-j][i]						# 20
				A[len(A)-1-j][i] = A[len(A)-i-1][len(A)-j-1]	# 22
				A[len(A)-1-i][len(A)-j-1] = A[j][len(A)-i-1]	# 20
				A[j][len(A)-1-i] = temp							# 00
