# Concept correct but taken from geeks for geeks
class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return a double
	def findMedianSortedArrays(self, A, B):
		if len(A) > len(B):		# B must be the larger list
			A,B = B,A
		m,n = len(A), len(B)

		if m == 0:
			if n == 0:
				return 0
			if n%2 != 0:				# odd
				return B[n/2]
			else:						# even
				return (B[n/2] + B[n/2-1]) / 2.0
		low = 0
		high = m
		while low <= high:
			i = (low+high)/2
			j = (m+n+1)/2 - i

			if (j == 0 or i == m or B[j-1] <= A[i]) and (i == 0 or j == n or A[i-1] <= B[j]):
				if (m+n)%2 != 0:
					if i == 0:
						return B[j-1]
					elif j == 0:
						return A[i-1]
					return max(A[i-1],B[j-1])
				else:
					if i == 0:



"""
http://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/

There are two sorted arrays A and B of size m and n respectively.

Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).

The overall run time complexity should be O(log (m+n)).

Sample Input

A : [1 4 5]
B : [2 3]

Sample Output

3
 NOTE: IF the number of elements in the merged array is even, then the median is the average of n / 2 th and n/2 + 1th element. 
For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5 
"""