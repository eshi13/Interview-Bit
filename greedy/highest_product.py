### Editorial

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
    	A.sort(reverse=True)
    	n = len(A) - 1

    	# All are positive
    	if (A[n] >= 0):
    		p = A[0] * A[1] * A[2]
		
		# Some are negative and positive
		elif (A[0] > 0):
			p = max(A[0] * A[1] * A[2], A[0] * A[n] * A[n-1])
		
		# All are negative
		elif (A[0] <= 0):
			p = A[0] * A[1] * A[2]
		return p

"""
Given an array of integers, return the highest product possible by multiplying 3 numbers from the array

Input:

array of integers e.g {1, 2, 3}
 NOTE: Solution will fit in a 32-bit signed integer 
Example:

[0, -1, 3, 100, 70, 50]

=> 70*50*100 = 350000

"""