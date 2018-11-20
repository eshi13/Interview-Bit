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


### Fastest
class Solution:
	# @param A: list of integers
	# @return an integer
	def maxp3(self, A):
		n = len(A)

		max1 = max(A)
		A.remove(max1)
		max2 = max(A)
		A.remove(max2)
		max3 = max(A)

		A.append(max1)
		A.append(max2)

		min1 = min(A)
		A.remove(min1)
		min2 = min(A)

		product = max(max1*max2*max3, max1*min1*min2)

		return product

### Lightweight
class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
    	arr = A
    	arr.sort()

    	return max(arr[-1]*arr[-2]*arr[-3], arr[-1]*arr[0]*arr[1])

    	if len(arr) < 3:
    		return 0

		three = [ float('-inf') for i in range(len(arr)) ]
		two = [ float ('-inf') for i in range (len(arr)) ]

		for i in range(1, len(arr)):
			for j in range(0, i):
				two[i] = max(arr[j] * arr[i], two[i])
				if i >= 2 and j >= 1:
					three[i] = max(two[j]*arr[i], three[i])
			# if i < 2:
            #     three[i] = float('-inf')
            # else:
            #     three[i] = two[i]*arr[i]
        return max(three)


"""
Given an array of integers, return the highest product possible by multiplying 3 numbers from the array

Input:

array of integers e.g {1, 2, 3}
 NOTE: Solution will fit in a 32-bit signed integer 
Example:

[0, -1, 3, 100, 70, 50]

=> 70*50*100 = 350000

"""