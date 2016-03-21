class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
    	firstChar = -1
    	n = len(A)
    	for i in xrange(n-2, -1, -1):
    		if A[i] < A[i+1]:
    			firstChar = i
    			break
    	if firstChar == -1:
    		return sorted(A)
    	
    	secondChar = firstChar + 1
    	left = firstChar + 1
    	right = n - 1

    	for i in xrange(left+1, right+1):
    		if A[firstChar] < A[i] and A[i] < A[secondChar]:
    			secondChar = i

    	A[firstChar], A[secondChar] = A[secondChar], A[firstChar]	# swap

    	A = A[:firstChar + 1] + sorted(A[firstChar+1:])
    	
    	return A

"""
0 1 2 3 4
---------
1 2 3 4 5

firstChar = 3
secondChar = 4
left = 4
right = 4

1 2 3 5 4
return A[0:4] - A[4:5]
"""