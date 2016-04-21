class Solution:
	# @param A : tuple of integers
	# @return a list of integers
	def repeatedNumber(self, A):
		sum_A, sum_A2, n = 0,0,0
		for a in A:
			sum_A2 += a*a
			sum_A += a
			n += 1
		sum_N = n*(n+1)/2

		res_A = sum_N - sum_A
		res_B = (sum_N * (2*n+1)/3 - sum_A2) / res_A
		x = (res_B - res_A)/2
		return [x, x+res_A] 
"""

You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4

------------

 Sum(Actual) = Sum(1...N) + A - B

    Sum(Actual) - Sum(1...N) = A - B. 

    Sum(Actual Squares) = Sum(1^2 ... N^2) + A^2 - B^2

    Sum(Actual Squares) - Sum(1^2 ... N^2) = (A - B)(A + B) 

    = (Sum(Actual) - Sum(1...N)) ( A + B). 
"""