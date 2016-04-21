class Solution:
	# @param A : integer
	# @return a strings
	def convertToTitle(self, A):
		res = ""
		while A >=0 :
			res.append(str((A-1)/ 26))+1)
			A %= 26
		return res

"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

	1 -> A
	2 -> B
	3 -> C
	...
	26 -> Z
	27 -> AA
	28 -> AB 
"""