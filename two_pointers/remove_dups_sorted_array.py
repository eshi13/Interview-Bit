class Solution:
	# @param A : list of integers
	# @return an integer
	def removeDuplicates(self, a):
		if (len(a) <= 1):
			return len(a)
		index = 1
		for i in xrange(1, len(a)):
			if a[i] != a[i-1]:
				temp = a[i]
				a[index] = a[i]
				index += 1
		return index