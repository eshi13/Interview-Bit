class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def subsetsWithDup(self, s):
		mySet = set([])
		s.sort()
		res = [[]]
		for e in s:
			for x in res:
				if x+[e] not in mySet:
					mySet.add(x+[e])
					res += x+[e]
		return sorted(res)
